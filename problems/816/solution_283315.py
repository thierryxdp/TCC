def maiores(lista,n):
    ''' Função que recebe uma lista e um número inteiro(n), e
        retorna outra lista, que contenha todos os números da
        lista original maiores que (n), ordenados em ordem
        crescente
        : param lista: list
        : param n: int
        : return: list  
    '''
    lista.append(num)
    lista.sort()
    del lista[:lista.index(n)]
    lista.remove(n)
    return lista