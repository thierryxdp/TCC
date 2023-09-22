def maiores(lista,n):
    '''função que dada uma lista de números inteiros e um número inteiro n, retorna outra lista, que contenha todos os números da lista original maiores que n.
    entrada: list
    saída: list'''
    list.sort(lista,reverse=True)
    return lista