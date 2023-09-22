def conta_frases(texto):
	"""Função que conta o número de frases que aparece em um texto
	Entrada: string
	Saída: int"""
	return texto.count("?") + texto.count("!") + (texto.count(".") - (3*texto.count("..."))) + texto.count("...")