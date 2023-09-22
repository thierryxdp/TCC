"""Recebe uma lista e um inteiro e retorna uma nova lista apenas com os numeros
da primeira lista que forem maiores que o inteiro.
list, int -> list"""

def maiores(lista, n):
    nova_lista = []
    for i in range(len(lista)+1):
        if lista[i] > n:
            nova_lista.append(lista[i])
	return nova_lista