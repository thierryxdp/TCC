def repetidos(x):
	"""Função em que dada uma lista x contendo números, retorna a quantidade de vezes que um elemento da lista é igual ao elemento anterior.
	list -> int"""
	i=0
	r=0
	while (i+1)<len(x):
		if x[i+1]==x[i]:
			r=r+1
		i=i+1
	return r