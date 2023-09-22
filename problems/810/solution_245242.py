def inverte(frase):
	frase = frase.replace('—',' ')
	frase = frase.replace(',',' ')
	frase = frase.replace(':',' ')
	frase = frase.replace('.',' ')
	frase = frase.replace(';',' ')
	frase = frase.replace('!',' ')
	frase = frase.replace('?',' ')
	frase = frase.replace('-',' ')
	frase = frase.lower()
	frase = frase.split()
	frase = list(reversed(frase))
	return (' '.join(frase))
	return frase