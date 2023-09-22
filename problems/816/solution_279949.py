def maiores(lista,n):
    '''Funcao que dada uma lista de numeros inteiros e um numero inteiro n,
    retorna outra lista, contendo todos os numeros da lista original
    maiores que n
    list, int -> list'''
    list.append(lista,n)
    list.sort(lista)
    posicao = list.index(lista,n)
    maior = posicao + 1
    return lista[maior:]