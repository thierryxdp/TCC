def soma_h(N):
	"""Função em que dado um número N calcula a série harmônica até o valor de N.
	int -> float"""
	H=0
	for x in range(1,N+1):
		H=H+1/x
	return round(H,2)

>>> def soma():
	S=0
	fatorial=1
	for x in range(1,11):
		fatorial=x*fatorial
		S=S+((-1)^(x+1)(11-x)/fatorial)
	return S