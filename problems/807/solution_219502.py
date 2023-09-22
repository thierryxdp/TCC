def conta_frases(texto):
	contagem2 = texto.split('!')
	contagem3 = texto.split('?')
	contagem4 = texto.split('...')
    contagem5 = texto.split('.')

	return len(contagem1) -1 + len(contagem2) - 1 + len(contagem3) - 1  + len(contagem4) -1