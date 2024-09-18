
# Introdução

Este projeto contém três exemplos de algoritmos que abordam o conceito de armazenamento de dados. Esses exemplos servem como uma introdução para entender como funciona um banco de dados, como manipular dados na memória, como gravá-los em arquivos, e como modelar essas operações usando orientação a objetos (OOP).

A compreensão desses conceitos é essencial para desenvolver sistemas mais robustos utilizando frameworks como Django, que é baseado no padrão **MVC (Model-View-Controller)**. O padrão MVC organiza o código em três componentes principais:

- **Model**: Responsável pela lógica de dados e interação com o banco de dados.
- **View**: Define como a interface do usuário será apresentada.
- **Controller**: Gerencia a comunicação entre o Model e a View, recebendo entradas do usuário e retornando as respostas corretas.

No Django, essa separação é fundamental para a construção de aplicativos web. Vamos primeiro entender os fundamentos com três versões de um sistema de gerenciamento de produtos e estoques.

---

## Algoritmo 1: Armazenamento apenas na memória

### Descrição

Neste primeiro exemplo, todos os dados de produtos e estoques são armazenados temporariamente na memória, ou seja, enquanto o programa estiver em execução. Quando o programa termina, todos os dados são perdidos.

### Como funciona

- As informações de **produto** e **estoque** são armazenadas em dicionários e listas na memória.
- A interação acontece através do menu, permitindo criar e listar produtos e estoques.
- Quando um produto ou estoque é criado, ele é armazenado em variáveis locais (listas).
- Ao listar produtos, o sistema exibe os dados diretamente da memória.

### Limitações

- Os dados são temporários. Quando o programa é fechado, os dados desaparecem.
- Este método é útil para entender como o armazenamento funciona na memória, mas não é prático para armazenar dados permanentemente.

### Exemplo de código

```python
produtos = []
estoques = []

def criar_produto():
    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto: "))
    quantidade = int(input("Quantidade: "))
    estoque = input("Estoque: ")
    produtos.append({"nome": nome, "preco": preco, "estoque": estoque, "quantidade": quantidade})
    print(f"Produto {nome} adicionado.")

def listar_produtos():
    for produto in produtos:
        print(f"{produto['nome']} - Preço: {produto['preco']} - Estoque: {produto['estoque']} - Quantidade: {produto['quantidade']}")
```

---

## Algoritmo 2: Armazenamento em arquivo de texto (TXT)

### Descrição

Neste segundo exemplo, os dados de produtos e estoques são armazenados em arquivos de texto. Aqui, introduzimos a ideia de persistência de dados, ou seja, os dados permanecem salvos mesmo após o programa ser encerrado.

### Como funciona

- Os produtos e estoques são armazenados em dois arquivos de texto separados (`produtos.txt` e `estoques.txt`).
- Cada vez que um novo produto ou estoque é criado, ele é gravado no arquivo correspondente.
- Ao listar os produtos, o sistema lê os arquivos para recuperar os dados.
- As operações de leitura e escrita simulam o comportamento de um banco de dados rudimentar.

### Vantagens

- Os dados são persistentes e não são perdidos quando o programa é encerrado.
- É uma forma simples de entender como um banco de dados armazena dados em arquivos, embora aqui estejamos usando um formato de texto simples.

### Exemplo de código

```python
def salvar_produto(nome, preco, estoque, quantidade):
    with open("produtos.txt", "a") as arquivo:
        arquivo.write(f"{nome},{preco},{estoque},{quantidade}
")
    print(f"Produto {nome} salvo no arquivo.")

def listar_produtos():
    try:
        with open("produtos.txt", "r") as arquivo:
            produtos = arquivo.readlines()
            for produto in produtos:
                nome, preco, estoque, quantidade = produto.strip().split(",")
                print(f"{nome} - Preço: {preco} - Estoque: {estoque} - Quantidade: {quantidade}")
    except FileNotFoundError:
        print("Nenhum produto encontrado.")
```

---

## Algoritmo 3: Orientação a Objetos (OOP)

### Descrição

Neste terceiro exemplo, utilizamos os princípios de **orientação a objetos (OOP)** para modelar os produtos e estoques. Cada produto e estoque é representado por uma classe, permitindo uma maior organização e modularidade do código.

### Como funciona

- Criamos duas classes principais: **Produto** e **Estoque**.
- A classe `Produto` tem métodos para salvar produtos em arquivos de texto e para listar ou atualizar produtos.
- A classe `Estoque` tem métodos para gerenciar os estoques, incluindo a criação e listagem de produtos por estoque.
- Este modelo se aproxima do padrão **Model** no Django, onde cada classe representaria uma tabela no banco de dados.

### Vantagens

- Código mais organizado e reutilizável.
- Introdução à modelagem de dados utilizando classes, que é uma base importante para frameworks como Django.
- Simula o comportamento de um sistema de banco de dados através de arquivos de texto, onde cada arquivo atua como uma "tabela".

### Exemplo de código

```python
class Produto:
    def __init__(self, nome, preco, estoque, quantidade):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        self.quantidade = quantidade

    def salvar(self):
        with open("produtos.txt", "a") as file:
            file.write(f"{self.nome},{self.preco},{self.estoque},{self.quantidade}
")
        print(f"Produto '{self.nome}' salvo com sucesso!")

class Estoque:
    def __init__(self, nome):
        self.nome = nome

    def salvar(self):
        with open("estoques.txt", "a") as file:
            file.write(f"{self.nome}
")
        print(f"Estoque '{self.nome}' salvo com sucesso!")
```

---

## Conclusão

Esses três algoritmos ajudam a entender como dados podem ser gerenciados e armazenados, seja temporariamente na memória, de forma persistente em arquivos, ou modelando estruturas mais complexas usando orientação a objetos.

Essa abordagem serve como base para aprender sobre **bancos de dados** e como manipulá-los usando **Modelos** no padrão **MVC**, um conceito central no desenvolvimento web com frameworks como **Django**. No Django, as tabelas do banco de dados são representadas por **Models**, e os dados são armazenados de forma persistente em bancos como SQLite, PostgreSQL, MySQL, entre outros.

O próximo passo seria aprender como o Django automatiza grande parte dessas tarefas de manipulação de dados e como ele se integra ao banco de dados para criar sistemas web completos.
