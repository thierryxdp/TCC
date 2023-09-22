def intercala(lista1, lista2):
    '''Função que, dadas duas listas com três elementos cada, retorna uma nova com os elementos de ambas intercaladas; list, list -> list.'''
    a = int(list(str(lista1[0])))
    b = int(list(str(lista2[0])))
    c = list(str(lista1[1]))
    d = list(str(lista2[1]))
    e = list(str(lista1[2]))
    f = list(str(lista2[2]))
    return a + b + c + d + e + f