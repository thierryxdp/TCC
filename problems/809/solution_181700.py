# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveisdef intercala(lista1, lista2):
    """dada duas listas, essa função intercala os elementos delas formando uma nova lista
    lista, lista -> lista"""
    l1 = [lista1]
    l2 = [lista2]
    l3 = l1 + l2
    l3[::2]
    l3[1::2]
    return l3