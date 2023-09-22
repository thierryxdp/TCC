def maiores(lista,n):
    '''Dados uma lista de números inteiros e um número
    inteiro n, retorna outra lista, que contenha todos os
    números da lista original maiores que n, ordenados em
    ordem crescente.
    list, int -> list'''
    if n in lista:
        list.sort(lista)
        inicio=list.index(lista,n)
        return lista[inicio+1:]
    else:
        list.append(lista,n)
        list.sort(lista)
        inicio=list.index(lista,n)
        return lista[inicio+1:]