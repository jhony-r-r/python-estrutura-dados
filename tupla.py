# Criando uma lista sobre alimentos
lista_alimentos = ['Arroz', 'Macarrão', 'Feijão', 'Carne', 'Batata', 'Abobrinha']
lista_valor = [29.99, 17.44, 10.28, 44.75, 9.18, 3.21]

# Transformando a lista em uma tupla através do método dict
transformar_alimento = tuple(lista_alimentos)
trasnformar_valor = tuple(lista_valor)

# Verificando o tipo que variável transformar possui
print(type(transformar_alimento))
print(type(trasnformar_valor))

# Retornando todos valores da tupla com sua estrutura
print(transformar_alimento)
print(trasnformar_valor)

# Retornando todos os valores da tuple sem sua estrutura

#Utilizando o laço de repetição FOR
for index in range (len(transformar_alimento) and len(trasnformar_valor)):
    print("O alimento", transformar_alimento[index], "possui o valor", trasnformar_valor[index])

#Utilizando o laço de repetição WHILE
count = 0
while count < len(lista_alimentos) and count < len(lista_valor):
    print("Alimentos do tipo", lista_alimentos[count], "possui valores de", lista_valor[count])
    count = count + 1

# Outra forma de retorar valores de maneira mais simplificada
for alimentos in transformar_alimento:
    print("Nome do alimento:", alimentos)


