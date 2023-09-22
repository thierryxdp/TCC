def maiores(lista, n):
    '''Dada uma lista e um numero n, retorna os numeros maiores que n.
    lista,int->lista'''
    lista.append(n)
    lista.sort()lista = lista[lista.index(n) + 1 : ]
    return lista