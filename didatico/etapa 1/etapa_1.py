# Lista de produtos na memória
produtos = []

# Funções CRUD
def criar_produto():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    estoque = input("Digite o estoque em que ele esta localizado: ")
    quantidade = float(input("Digite a quantidade do produto: "))
    produto = {"id": len(produtos) + 1, "nome": nome, "preco": preco , "estoque":estoque, "quantidade": quantidade}
    produtos.append(produto)
    print(f"Produto '{nome}' cadastrado com sucesso!")

def listar_estoques():
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

def listar_produtos():
    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
    else:
        print("\nLista de Produtos:")
        for produto in produtos:
            print(f"ID: {produto['id']} | Nome: {produto['nome']} | Preço: R$ {produto['preco']} | Estoque: {produto['estoque']} | Quantidade: {produto['quantidade']}")
        print()

def atualizar_produto():
    listar_produtos()
    id = int(input("Digite o ID do produto que deseja atualizar: "))
    for produto in produtos:
        if produto['id'] == id:
            nome = input(f"Digite o novo nome do produto (atual: {produto['nome']}): ")
            preco = float(input(f"Digite o novo preço do produto (atual: R$ {produto['preco']}): "))
            estoque = input(f"Digite o novo estoque em que ele esta localizado (atual: R${produto['estoque']}): ")
            quantidade = float(input(f"Digite a nova quantidade(atual: R${produto['quantidade']}):"))
            produto['nome'] = nome
            produto['preco'] = preco
            produto['estoque'] = estoque
            produto['quantidade'] = quantidade
            print(f"Produto ID {id} atualizado com sucesso!")
            return
    print("Produto não encontrado.")

def deletar_produto():
    listar_produtos()
    id = int(input("Digite o ID do produto que deseja deletar: "))
    global produtos
    produtos = [produto for produto in produtos if produto['id'] != id]
    print(f"Produto ID {id} removido com sucesso!")

# Loop interativo
def menu():
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
            criar_produto()
        elif opcao == '2':
            listar_produtos()
        elif opcao == '3':
            listar_estoques()
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
