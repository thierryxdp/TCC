def posLetra(s,l,n):
	"""Função em que dada uma string s, uma letra l e um valor de ocorrência n, retorna a posição da letra l na string s em sua n-ésima vez.
	string, string, int -> int"""
	if s.count(l)<n:
		return -1
	else:
		i=0
		s=list(s)
		while i<(n-1):
			if s.index(l)!=0:
				k=s.index(l)+1
				s[:k]='x'*(s.index(l))
			else:
				s[:s.index(l)+1]='x'
			i=i+1
		return s.index(l)