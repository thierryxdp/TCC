def insere(lista_numero, n):
	'''Dada uma lista de números inteiros e um número 
    inteiro n, inclui n na posição correta de maneira 
    crescente ordenada.
    list, int -> list'''
    lista_numero.append(n)
    return lista_numero.sort()