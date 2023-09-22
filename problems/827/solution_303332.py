def qtd_divisores(n):
	"""Função em que dado um número n retorna a quantidade de divisores inteiros deste n.
	int -> int"""
	q=0
	for x in range(1,n+1):
		if n%x==0:
			q=q+1
	return q