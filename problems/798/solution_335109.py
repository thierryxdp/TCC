def freq_palavras(frases):
	'''Recebe uma frase e retorna um dicionario com o numero de aparições
	de cada palavra nesta frase.
    str -- > dict(str:int)'''

	palavras = frases.split()
	dicionario = {}
	for i in palavras:
		dicionario[i] = palavras.count(i)
	return dicionario