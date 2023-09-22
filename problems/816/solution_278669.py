def maiores(lista, n):
    '''Função que dada uma lista de números
    inteiros e um número inteiro n, retorna
    uma lista que tenha todos os números
    da lista original que são maiores que n.'''
    list.sort(lista)
    lista1 = lista[n-1:]
    return lista