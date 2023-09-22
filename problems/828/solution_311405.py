def primo(n):
	"""Função em que dado um número n retorna se este é primo ou não.
	int -> boolean"""
	from math import ceil
	if n==1 or n==2:
		return False
	for x in range(2,ceil((n+1)/2)):
		if n%x==0:
			return False
	return True