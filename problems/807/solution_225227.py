def conta_frases(frase):
   	"""função que retorna o nuemro de palavras em uma frase passada
    como entrada,str>int"""
	frase = s.str.split(frase)
	return len(frase)