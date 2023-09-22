def intercala(lista1, lista2):
    '''Função que, dadas duas listas com três elementos cada, retorna uma nova com os elementos de ambas intercaladas; list, list -> list.'''
    a = list.split(lista1)
    b = list.split(lista2)
    return a[0] + b[0] + a[1] + b[1] + a[2] + b[2]