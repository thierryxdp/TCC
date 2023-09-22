def maiores(lista, n):
    '''Dada uma lista de numeros inteiros e um numero inteiro n, retorna outra lista que contenha todos os numeros da lista maior do que n
    list, int -> list'''
    list.append(lista, n)
    list.sort(lista)
    posicao_n=list.index(lista, n)
    return lista[(posicao_n+1):]