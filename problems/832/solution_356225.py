def eh_quadrada(M):
	"""Função em que dada uma matriz M retorna se está é quadrada ou não.
	list -> boolean"""
	if M==[]:
		return True
	else:
		return len(M)==len(M[0]