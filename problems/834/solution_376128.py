def media_matriz(M):
	"""Função em que dada uma matriz M de inteiros não vazios, retorna a média de todos os números da matriz com duas casas decimais de precisão.
	list -> int"""
	s=0
	d=0
	for i in range(len(M)):
		for j in M[i]:
			s=s+j
			d=d+1
	return round(s/d,2)