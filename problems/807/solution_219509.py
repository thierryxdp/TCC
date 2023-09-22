def conta_frases(texto):
	contagem1 = texto.split('.')
	contagem2 = texto.split('!')
	contagem3 = texto.split('?')
	contagem4 = texto.count('...')

	return len(contagem1) + len(contagem2) + len(contagem3) - 4