def conta_numero(n,M):
	"""Função em que dado um número n e uma matriz M, retorna quantas vezes n aparece em M.
	int, list -> int"""
	c=0
	for i in range(len(M)):
		for j in M[i]:
			if j==n:
				c=c+1
	return c