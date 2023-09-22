def soma_h(N):
	"""Função em que dado um número N calcula a série harmônica até o valor de N.
	int -> int"""
	H=0
	for x in range(1,N+1):
		H=H+1/x
	return round(H,2)