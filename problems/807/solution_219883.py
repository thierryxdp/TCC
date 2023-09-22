def conta_frases(texto):
	numFrases = 0
	numFrases += texto.count('.')
	numFrases += texto.count('...')
	numFrases += texto.count('!')
	numFrases += texto.count('?')
	return numFrases