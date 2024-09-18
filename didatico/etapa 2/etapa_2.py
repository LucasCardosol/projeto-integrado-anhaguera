# Nome do arquivo onde os dados serão armazenados
ARQUIVO = 'produtos.txt'
produtos = []
def ler_dados():
    """Ler os dados do arquivo e retornar uma lista de produtos."""
    
    try:
        with open(ARQUIVO, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                partes = linha.strip().split('|')
                if len(partes) == 5:
                    produto = {
                        "id": int(partes[0]),
                        "nome": partes[1],
                        "preco": float(partes[2]),
                        "estoque": partes[3],
                        "quantidade": float(partes[4])
                    }
                    produtos.append(produto)
    except FileNotFoundError:
        # Arquivo não encontrado, retorna lista vazia
        return produtos
    return produtos

def escrever_dados(produtos):
    """Escrever os dados no arquivo."""
    with open(ARQUIVO, 'w') as arquivo:
        for produto in produtos:
            linha = f"{produto['id']}|{produto['nome']}|{produto['preco']}|{produto['estoque']}|{produto['quantidade']}\n"
            arquivo.write(linha)

# Funções CRUD
def criar_produto(produtos):
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    estoque = input("Digite o estoque em que ele está localizado: ")
    quantidade = float(input("Digite a quantidade do produto: "))
    produto = {"id": len(produtos) + 1, "nome": nome, "preco": preco, "estoque": estoque, "quantidade": quantidade}
    produtos.append(produto)
    escrever_dados(produtos)
    print(f"Produto '{nome}' cadastrado com sucesso!")

def listar_estoques(produtos):
    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
    else:
        # Organizar produtos por estoque
        estoques = {}
        for produto in produtos:
            estoque = produto['estoque']
            if estoque not in estoques:
                estoques[estoque] = []
            estoques[estoque].append(produto)
        
        print("\nLista de Estoques e Produtos:")
        for estoque, itens in estoques.items():
            print(f"\nEstoque: {estoque}")
            for produto in itens:
                print(f"  - {produto['nome']} | Quantidade: {produto['quantidade']}")
        print()

def listar_produtos(produtos):
    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
    else:
        print("\nLista de Produtos:")
        for produto in produtos:
            print(f"ID: {produto['id']} | Nome: {produto['nome']} | Preço: R$ {produto['preco']} | Estoque: {produto['estoque']} | Quantidade: {produto['quantidade']}")
        print()

def atualizar_produto(produtos):
    listar_produtos(produtos)
    id = int(input("Digite o ID do produto que deseja atualizar: "))
    for produto in produtos:
        if produto['id'] == id:
            nome = input(f"Digite o novo nome do produto (atual: {produto['nome']}): ")
            preco = float(input(f"Digite o novo preço do produto (atual: R$ {produto['preco']}): "))
            estoque = input(f"Digite o novo estoque em que ele está localizado (atual: {produto['estoque']}): ")
            quantidade = float(input(f"Digite a nova quantidade (atual: {produto['quantidade']}): "))
            produto['nome'] = nome
            produto['preco'] = preco
            produto['estoque'] = estoque
            produto['quantidade'] = quantidade
            escrever_dados(produtos)
            print(f"Produto ID {id} atualizado com sucesso!")
            return
    print("Produto não encontrado.")

def deletar_produto(produtos):
    listar_produtos(produtos)
    id = int(input("Digite o ID do produto que deseja deletar: "))
    
    produtos = [produto for produto in produtos if produto['id'] != id]
    escrever_dados(produtos)
    print(f"Produto ID {id} removido com sucesso!")

# Loop interativo
def menu():
    produtos = ler_dados()
    
    while True:
        print("\n=== Sistema de Gerenciamento de Produtos ===")
        print("1. Cadastrar Produto")
        print("2. Listar Produtos")
        print("3. Listar Estoques")
        print("4. Editar Produto")
        print("5. Deletar Produto")
        print("6. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            criar_produto(produtos)
        elif opcao == '2':
            listar_produtos(produtos)
        elif opcao == '3':
            listar_estoques(produtos)
        elif opcao == '4':
            atualizar_produto(produtos)
        elif opcao == '5':
            deletar_produto(produtos)
        elif opcao == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o menu
menu()
