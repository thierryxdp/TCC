def maiores (lista,n):
    '''
    retorna uma nova lista com numeros maiores que n ordenados em ordem crescente
    list, int -> list
    '''
    lista.append(n)
    lista.sort()
    lista=lista[lista.index(n)+1:]
    return lista