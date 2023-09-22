def posLetra(s,l,n):
	i = 0
	ocorrencia = 0
	while i < len(s):
		if(s[i] == l):
			ocorrencia += 1
		if ocorrencia == n:
			return i
	return -1