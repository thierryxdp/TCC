def conta_frases(texto):
    ponto = texto.find('.')
    exclamacao = texto.find('!')
	interrogacao = texto.find('?')
	reticencias = texto.find('...')
    return texto[:ponto]