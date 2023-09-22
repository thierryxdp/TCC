def maiores(lista, n):
    '''Função que dada uma lista de números
    inteiros e um número inteiro n, retorna
    uma lista que tenha todos os números
    da lista original que são maiores que n.'''
    lista1 = list.sort(lista)
    lista2 = lista1[0:n]
    return lista