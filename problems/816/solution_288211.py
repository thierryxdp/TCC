def maiores(lista,n):
    '''Função que dada uma lista de números inteiros e um número inteiro n, retorna outra lista
    que contenha todos os números da lista original maiores que n, ordenados em ordem crescente'''
    l = lista = [n]
    list.sort(l)
    a = list.index(l,n)
    return l[a:]