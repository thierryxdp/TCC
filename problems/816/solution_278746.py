def maiores(lista_int,n):
    '''Funcao que recebe uma lista de numeros inteiros, um numero inteiro n
        e retorna uma outra lista com todos os numeros da lista original que
        sao maiores que n.'''
    list.insert(lista_int,0,n)
    list.sort(lista_int,reverse=True)
    x = list.index(lista_int,n,0)
    del lista_int[x::]

    return lista_int[::-1]