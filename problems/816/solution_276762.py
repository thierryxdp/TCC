def maiores(lista, n):
    '''função que dada uma lsita de números inteiros e um número inteiro n,
    retorna outra lista que contenha todos os números da lista original
    maiores que n; list, int -> list'''
    list.sort(lista)
    if n in lista:
        i = list.index(lista, n)
        return lista[i+1:]
    	elif n < lista[0]
        return lista