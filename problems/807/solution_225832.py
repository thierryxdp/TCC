def conta_frases (texto):
	"""Dado o texto de entrada, retorna o número de frases desse texto. str -> int"""
	return str.count(texto, ".") + str.count(texto, "!") + str.count(texto, "?") + str.count(texto, "...")