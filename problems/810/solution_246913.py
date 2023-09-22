def inverte(frase):
	frase= frase.replace('-','')
	frase=frase.replace('.','')
	frase=frase.replace('!','')
	frase=frase.replace('?','')
	frase=frase.replace(',','')
	frase = frase.lower()
	lista = str.split(frase)
	lista.reverse()
	frase=str.join(' ',lista)
	return frase