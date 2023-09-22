def faltante(l):
	"""Função em que dada uma lista com n-1 inteiros numerados de 1 a N retorna o número inteiro entre 1 e N que está faltando.
	list -> int"""
	i=0
	k=l[-1]+1
	while i<len(l) and k==l[-1]+1:
		if l[i]!=(i+1):
			k=i+1
		i=i+1
	return k