'''Recebe uma lista de inteiros e um numero inteiro n. Retorna 
uma lista com os numeros da lista original maiores que n
list, int -> list'''

def maiores(lista, n):
	list.insert(lista, 0, n)
    list.sort(lista)
    posicao = list.index(lista, n) + 1
    return lista[posicao:]