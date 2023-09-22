def posLetra(s,l,n):
	"""Função em que dada uma string s, uma letra l e um valor de ocorrência n, retorna a posição da letra l na string s em sua n-ésima vez.
	string, string, int -> int"""
	if s.count(l)<n:
		return -1
	else:
		i=0
		while i<(n):
			if s.index(l)!=0:
				s[:s.index(l)]='x'*(s.index(l))
			else:
				s[:s.index(l)]='x'
			i=i+1
		return s.index(l)