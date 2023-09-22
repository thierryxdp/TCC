# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Dado as entradas lista1 e lista2 retorna uma lista 3 que é a intercalação das listas anteriores"""
    return list({lista1[0],lista2[0],lista1[1],lista2[1],lista1[2],lista2[2]})