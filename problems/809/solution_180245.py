# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """função que dadas duas listas de tamanho 3 gera uma lista que é formada a partir dos elementos das duas listas de forma intercalada"""
    lista3=lista1+lista2
    lista3[::2]=lista1
    lista3[1::2]=lista2
    return lista3