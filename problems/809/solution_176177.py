def intercala(lista1, lista2):
    '''Intercala duas listas de tamanho 3
    list, list -> list'''
    lista3 = []
    if lista1[0] < lista2[0]:
        lista3 += lista1[0]
        lista3 += lista2[0]
    else:
        lista3 += lista2[0]
        lista3 += lista1[0]

    if lista1[1] < lista2[1]:
        lista3 += lista1[1]
        lista3 += lista2[1]
    else:
        lista3 += lista2[1]
        lista3 += lista1[1]

    if lista1[2] < lista2[2]:
        lista3 += lista1[2]
        lista3 += lista2[2]
    else:
        lista3 += lista2[2]
        lista3 += lista1[2]

    return lista3