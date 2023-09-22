def maiores(lista, n):
    '''Dada uma lista de numeros inteiros e um numero
    inteiro 'N', retorna uma lista contendo os numeros
    os numeros da lista original maiores que 'N', ordenados em ordem crescente;
    list, int -> list'''
    lista.sort()
	return lista[lista.index(n) + 1:len(lista)]