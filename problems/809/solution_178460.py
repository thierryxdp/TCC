def intercala(lista1, lista2):
    '''função que dados elementos da lista1 e da lista2, retorna uma lista3 com tais elementos intercalados.
    entrada:list, list
    saída: list'''
    lista3 = (lista1[0:3]) + (lista2[0:3])
    return sorted(lista3)