# Criando uma lista para armazenar cidades do paraná
cidades_parana = [
    "Curitiba",
    "Londrina",
    "Telêmaco Borba",
    "Ortigueira",
    "Ponta Grossa",
    "Colombo",
    "Maringá",
    "Castro",
    "Arapoti",
    "Ipiranga",
    "Sarandi",
    "Campo Morão",
    "Cianorte",
    "Pinhais",
    "Irati",
    "Guarapuava"
]

# Criando outra lista para juntar está com a lista anterior
todas_cidades = [
    "São Paulo",
    "Rio de Janeiro",
    "Fortaleza",
    "Belo Horizonte",
    "Recife",
    "Salvador"]

# Adicionar valor na lista
cidades_parana.append("Tibagi")

# Remover valor da lista através do nome especificado
cidades_parana.remove("Sarandi")

# Inverter valores da lista
cidades_parana.reverse()

# Colocando lista em ordem alfabético
cidades_parana.sort()

# Juntando valores de listas
cidades_parana.extend(todas_cidades)

# Inserindo valor especificado através de índice de uma lista
cidades_parana.insert(4,  "Pato Branco")

# Remover valor da lista através de índice
cidades_parana.pop(9)

# Copiando valores da lista e alocando em uma nova lista
cidades_parana_copiado = cidades_parana.copy()

# Retornando o índice do valor indicado ao método
index = cidades_parana_copiado.index("Telêmaco Borba")

# Limpando a lista
cidades_parana.clear()

paises = ["Brasil", 1, "Espanha", 3, "Espanha", "1", "Brasil", 1, 1, 3]
# Retorna o número de vezes que o valor declarado aparece na lista
contador = paises.count("Brasil")

print(contador)
print(index)
print(cidades_parana_copiado)

# Outro tipo de lista
lista_contato = [
    ["Elias", 22223333],
    ["Hernandez", 33332222],
    ["Matias", 11113333],
    ["Hugo", 44442222]
]

print("O",lista_contato[3][0], "possui o número de contato", lista_contato[3][1])

