def posLetra(frase,letra,n):
	qtd_letras = str.count(frase,letra)
	
	if qtd_letras < n:
		return -1
	i = 0
	c = 0
	while i < len(frase):
		if frase[i] == letra:
			c += 1
		if c == n:
			return i
		i += 1
	return c