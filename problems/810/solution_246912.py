def inverte(frase):
	simbolos ='?,!-.'
	for c in simbolos.split():
		frase=frase.replace(c,'')
		frase=frase.lower()
		lista=str.split(frase)
		lista.reverse()
		frase=str.join(' ',lista)
		return frase