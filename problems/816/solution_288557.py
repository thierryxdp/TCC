def maiores(lista, n):
    '''Dada uma lista de números inteiros e um número
    inteiro n, retorna outra lista, que contém todos os
    números da lista original maiores que n, ordenados
    em ordem crescente.'''
    i = n
    lista.append(i)
    lista.index(i)
    lista.sort()
    
    return lista[i+1:]