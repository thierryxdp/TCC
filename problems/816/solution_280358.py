def maiores (lista,n):
    '''função que dada uma lista de números inteiros
    e um inteiro, retorne outra lista que contenha todos os
    números da lista original maiores que n
    list, int -> list'''
    maiores_numeros = []
    for c in lista:
        if c > n:
            maiores_numeros.append(c)
    return maiores_numeros.sort[]