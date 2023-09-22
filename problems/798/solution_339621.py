def freq_palavras(frase):

	resp = {}
	frase = frase.split()

	i = 0
	while i<len(frase):
		resp[frase[i]] = frase.count(frase[i])
		i += 1

	return resp