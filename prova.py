class Livro:
    def __init__(self, nome, ano):
        self.__nome = nome
        self.ano = ano

    def get_nome(self):
        return self.__nome
    def set_nome(self, novo_nome):
        self.__nome = novo_nome

    def get_ano(self):
        return self.ano 
    def set_ano(self, ano_correto):
        self.ano = ano_correto

class Informacoes:
    def __init__(self, autor, preco, genero):
        self.autor = autor
        self.genero = genero
        self.__preco = preco

    def get_autor(self):
        return self.autor
    def set_autor(self, autor_certo):
        self.autor = autor_certo

    def get_preco(self):
        return self.__preco
    def set_preco(self, preco_x):
        self.__preco = preco_x

    def get_genero(self):
        return self.genero
    def set_genero(self, genero_y):
        self.genero = genero_y

livro = Livro("Calvos", 2009)

variavel = "livro"

print(variavel)

livro.set_nome("Nome: Carlos Eduardo")
livro.set_ano(2008)

print(livro.get_nome(), livro.get_ano())

informacoes = Informacoes("Luvas Brais", "R$ 208", "Filosofia")

informacoes.set_autor("Autor: Lucas R.")
informacoes.set_genero("Gênero: Conhecimento")
informacoes.set_preco("Preço: R$2008")

print(informacoes.get_autor(), informacoes.get_genero(), informacoes.get_preco())

pergunta = str(input("O que é Pipeline?: "))
if pergunta != "?":
    print("É um processo de construção automatizado")
else: 
    print("Você sabo")

pergunta2 = str(input("O que são requisitos funcionais e não funcionais?: "))
if pergunta != "]":
    print("Requisitos funcionais são aqueles que o usuário pode interagir, como botões ou barra de pesquisa\nNão funcionais são aqueles que o usuário não vê e não pode interagir, como segurança e usuabilidade.")
else: 
    print("você sabe demais")

pergunta3 = str(input("Quais os pilares do modelo cascata?"))
if pergunta3 != "R":
    print("Levantamento de requisitos, Planejamentos, Desenvolvimento, Teste, implementação e Manutenção")
else:
    print("fake")