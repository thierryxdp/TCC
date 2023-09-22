def maiores(lista, n):
    '''Dado uma lista e um numero n, retorna os numeros maiores que n
    Lista, int->Lista'''
    lista.append(n)
    lista.sort()
    lista = lista[lista.index(n) + 1 : ]
    return lista