def inverte(frase):
	simbolos_pontuacao='!',',','?','.'
	for c in simbolos_pontuacao:
        if c in frase:
		frase=frase.replace(c,'')
		lista=str.split(frase)
		lista.reverse()
		frase=str.join(' ',lista)
		return frase