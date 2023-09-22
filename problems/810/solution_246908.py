def inverte(frase):
	type(frase) == str
    simbolos_pontuacao=',?.!'
	for c in simbolos_pontuacao:
		frase = frase.replace(c, '')
		lista=str.split(frase)
		lista.reverse()
		frase=str.join(' ',lista)
		return frase