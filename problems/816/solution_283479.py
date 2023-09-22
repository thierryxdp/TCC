def maiores(listanumeros,n):
    '''Retorna uma lista de numeros inteiros que sao maiores que um numeor n, list->list'''
    listanumeros.append(n)
    list.sort(listanumeros)
    lista=listanumeros[list.index(listanumeros,n)+1:]
    return lista