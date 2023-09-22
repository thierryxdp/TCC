def filtra_pares(n):
	"""Dada uma tupla com 4 números inteiros, retorna uma nova tupla sem os ímpares"""
	tupla = ()
	if n[0]%2 == 0:
	tupla += (n[0],)
	if n[1]%2 == 0:
	tupla += (n[1],)
	if n[2]%2 == 0:
	tupla += (n[2],)
	if n[3]%2 == 0:
	tupla += (n[3],)
	return tupla