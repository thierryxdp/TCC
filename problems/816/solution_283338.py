def maiores (lista,n):
    '''
    retorna uma nova lista com numeros maiores que n ordenados em ordem crescente
    list, int -> list
    '''
    return (lista.append(n) and lista.sort() and lista=lista[lista.index(n)+1:]