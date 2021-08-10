# Criando o dicionario relacionado a livros
dicionario_livros = {
    "Nome" : "O Pequeno Principe",
    "Autor" : "Antoine de Saint-Exupéry",
    "Ano de lançamento" : 1943,
    "Gênero" : "Ficção"
}

# Mostrando às chaves, valores e ambos
print(
    dicionario_livros, 
    "Retornando chave do livro: ", dicionario_livros.keys(), 
    "Retornando valores do livro:", dicionario_livros.values(), 
    "Retornando chave e valor de livro:", dicionario_livros.items()
    )

# Transformando listas em dicionários
listas_produtos = []

# Transformando através do método 'dict'
dicionario_produtos = dict(listas_produtos)
print(type(dicionario_produtos))

#Transformando dicionário em lista
lista_livros = []
# Transformando o dicionário relacionado a livros em uma lista organizada
lista_livros = list(dicionario_livros.items())
# Podemos envês de dicionário.items, utilizar às 'Keys' ou 'Values', porém não retorna por completo

print("Que tipo de estrutura é ? ", type(lista_livros), lista_livros)