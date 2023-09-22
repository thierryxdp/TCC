def maiores(inteiros, n):
    '''Dada uma lista de números inteiros e um inteiro n, retorna uma lista
    que contém todos os números da lista original maiores que n'''
    list.append(inteiros, n)
    list.sort(inteiros)
    m=list.index(inteiros,n)
    return inteiros[m+1:]