# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """função que dadas duas listas, com três valores cada, retorna uma nova lista com os valores das duas primeiras, intercaladas; list, list-->list"""
    lista1= lista1[0,1,2]
    lista2= lista2[0,1,2]
    lista_nova= [lista1[0],lista2[0],lista1[1],lista2[1],lista1[2],lista2[2]]
    return lista_nova