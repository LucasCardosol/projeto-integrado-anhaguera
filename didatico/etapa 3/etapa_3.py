import os

# Classe Produto
class Produto:
    def __init__(self, nome, preco, estoque, quantidade):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        self.quantidade = quantidade
    
    # Método para salvar o produto em produtos.txt
    def salvar(self):
        with open("produtos.txt", "a") as file:
            file.write(f"{self.nome},{self.preco},{self.estoque},{self.quantidade}\n")
        print(f"Produto '{self.nome}' salvo com sucesso!")
    
    # Método para atualizar um produto no arquivo
    @staticmethod
    def atualizar(nome_antigo, novo_nome, novo_preco, novo_estoque, nova_quantidade):
        produtos = Produto.carregar_produtos()
        with open("produtos.txt", "w") as file:
            for produto in produtos:
                if produto['nome'] == nome_antigo:
                    file.write(f"{novo_nome},{novo_preco},{novo_estoque},{nova_quantidade}\n")
                else:
                    file.write(f"{produto['nome']},{produto['preco']},{produto['estoque']},{produto['quantidade']}\n")
        print(f"Produto '{nome_antigo}' atualizado com sucesso!")

    # Método para deletar um produto
    @staticmethod
    def deletar(nome):
        produtos = Produto.carregar_produtos()
        with open("produtos.txt", "w") as file:
            for produto in produtos:
                if produto['nome'] != nome:
                    file.write(f"{produto['nome']},{produto['preco']},{produto['estoque']},{produto['quantidade']}\n")
        print(f"Produto '{nome}' removido com sucesso!")

    # Método para carregar os produtos do arquivo
    @staticmethod
    def carregar_produtos():
        produtos = []
        if os.path.exists("produtos.txt"):
            with open("produtos.txt", "r") as file:
                for linha in file:
                    nome, preco, estoque, quantidade = linha.strip().split(",")
                    produtos.append({"nome": nome, "preco": float(preco), "estoque": estoque, "quantidade": int(quantidade)})
        return produtos

# Classe Estoque
class Estoque:
    def __init__(self, nome):
        self.nome = nome

    # Método para salvar o estoque em estoques.txt
    def salvar(self):
        with open("estoques.txt", "a") as file:
            file.write(f"{self.nome}\n")
        print(f"Estoque '{self.nome}' salvo com sucesso!")
    
    # Método para listar produtos por estoque
    @staticmethod
    def listar_produtos_por_estoque():
        produtos = Produto.carregar_produtos()
        estoques = Estoque.carregar_estoques()
        
        if len(produtos) == 0:
            print("Nenhum produto cadastrado.")
            return

        print("\nLista de Estoques e Produtos:")
        for estoque in estoques:
            print(f"\nEstoque: {estoque}")
            itens = [produto for produto in produtos if produto['estoque'] == estoque]
            if itens:
                for produto in itens:
                    print(f"  - {produto['nome']} | Quantidade: {produto['quantidade']}")
            else:
                print("  - Nenhum produto cadastrado nesse estoque.")
        print()

    # Método para carregar os estoques do arquivo
    @staticmethod
    def carregar_estoques():
        estoques = []
        if os.path.exists("estoques.txt"):
            with open("estoques.txt", "r") as file:
                for linha in file:
                    estoques.append(linha.strip())
        return estoques

# Funções auxiliares para interagir com o usuário
def criar_produto():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade do produto: "))

    # Verificar se existem estoques cadastrados
    estoques = Estoque.carregar_estoques()
    
    if not estoques:
        print("Nenhum estoque encontrado. Será necessário criar um novo estoque.")
        estoque = criar_novo_estoque()
    else:
        print("\nEscolha uma das opções:")
        print("1. Usar um estoque existente")
        print("2. Criar um novo estoque")
        opcao = input("Opção: ")

        if opcao == '1':
            print("\nEstoque(s) disponível(is):")
            for idx, est in enumerate(estoques, start=1):
                print(f"{idx}. {est}")
            escolha = int(input("\nEscolha o número do estoque: ")) - 1
            estoque = estoques[escolha]
        elif opcao == '2':
            estoque = criar_novo_estoque()
        else:
            print("Opção inválida.")
            return

    produto = Produto(nome, preco, estoque, quantidade)
    produto.salvar()

def criar_novo_estoque():
    nome_estoque = input("Digite o nome do novo estoque: ")
    estoque = Estoque(nome_estoque)
    estoque.salvar()
    return nome_estoque

def atualizar_produto():
    nome_antigo = input("Digite o nome do produto que deseja atualizar: ")
    novo_nome = input(f"Digite o novo nome do produto (atual: {nome_antigo}): ")
    novo_preco = float(input(f"Digite o novo preço do produto: "))
    novo_estoque = input(f"Digite o novo estoque: ")
    nova_quantidade = int(input(f"Digite a nova quantidade: "))
    
    # Verifica se o novo estoque existe
    estoques = Estoque.carregar_estoques()
    if novo_estoque not in estoques:
        print(f"Estoque '{novo_estoque}' não encontrado. Por favor, crie o estoque primeiro.")
        return
    
    Produto.atualizar(nome_antigo, novo_nome, novo_preco, novo_estoque, nova_quantidade)

def deletar_produto():
    nome = input("Digite o nome do produto que deseja deletar: ")
    Produto.deletar(nome)

def criar_estoque():
    nome = input("Digite o nome do novo estoque: ")
    estoque = Estoque(nome)
    estoque.salvar()

# Menu principal
def menu():
    while True:
        print("\n=== Sistema de Gerenciamento de Produtos ===")
        print("1. Cadastrar Produto")
        print("2. Cadastrar Estoque")
        print("3. Listar Estoques e Produtos")
        print("4. Editar Produto")
        print("5. Deletar Produto")
        print("6. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            criar_produto()
        elif opcao == '2':
            criar_estoque()
        elif opcao == '3':
            Estoque.listar_produtos_por_estoque()
        elif opcao == '4':
            atualizar_produto()
        elif opcao == '5':
            deletar_produto()
        elif opcao == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o menu
menu()
