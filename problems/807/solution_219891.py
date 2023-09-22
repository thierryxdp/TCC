def conta_frases(texto):
	numFrases = 0
	texto = texto.replace('...','.')
	numFrases += texto.count('.')
	numFrases += texto.count('...')
	numFrases += texto.count('!')
	numFrases += texto.count('?')
	return numFrases