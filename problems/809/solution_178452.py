# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """ Dada duas listas, essa função gera uma nova lista contendo todos os valores das duas
    list -> list"""
    lista3 = lista1 + lista2
    lista3[::2] = lista1
    lista3[1::2] = lista2
    return lista3