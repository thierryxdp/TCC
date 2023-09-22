def maiores(lista, n):
    '''Dada uma lista de números inteiros e um número
    inteiro n, retorna outra lista, que contém todos os
    números da lista original maiores que n, ordenados
    em ordem crescente.'''
    lista.append(n)
    lista.sort()
    i = lista.index(n)
    
    return lista[i+1:]