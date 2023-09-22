# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """dada duas listas, essa função intercala os elementos delas formando uma nova lista
    lista, lista -> lista"""
    l1 = [x]
    l2 = [y]
    l3 = l1 + l2
    l3[::2] = l1
    l3[1::2] = l2
    return l3