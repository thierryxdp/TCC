def maiores(lista,n):
    '''
    dado uma lista e um numero inteiro n
    retorna outra lista com todos os numeros maiores que n
    '''
    lista[0:0]=[n]
    list.sort(lista)
    del[list.index(lista,n)]
    return lista