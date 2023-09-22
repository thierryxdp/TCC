def maiores(lista, n):
    '''função que dada uma lsita de números inteiros e um número inteiro n,
    retorna outra lista que contenha todos os números da lista original
    maiores que n; list, int -> list'''
    if n in lista:
        list.sort(lista)
        i = list.index(lista, n)
        return lista[i+1:]
    else:
        return lista