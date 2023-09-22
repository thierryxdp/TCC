def maiores (lista,n):
    '''função que dada uma lista de números inteiros
    e um inteiro, retorne outra lista que contenha todos os
    números da lista original maiores que n
    list, int -> list'''
    if n not in lista:
        lista.append(n)
        lista.sort()
        a = lista.index(n)
        lista_numeros = lista[a+1:]
        rep = lista_numeros.count(n)
        return lista_numeros[rep:]