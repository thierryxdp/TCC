def filtraMultiplos(x,n):
	"""Função em que dada uma lista x de números inteiros e um número inteiro n, retorna uma lista com todos os números da lista x divisíveis por n.
	list, int -> list"""
	cont=0
	while cont<len(x):
		if x[cont]%n ==0:
			del x[cont]
		cont=cont+1
	return x