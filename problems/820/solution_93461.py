def posLetra(s,l,n):
	"""Função em que dada uma string s, uma letra l e um valor de ocorrência n, retorna a posição da letra l na string s em sua n-ésima vez.
	string, string, int -> int"""
	if s.count(l)<n:
		return -1
	else:
		i=0
		while i<(n-1):
			s=s[s.index(l):]
			i=i+1
		return s.index(l)