def conta_frases(txt):
	"""funcao que conta as frases de um texto, sendo o termino da frase determinados por pontos dinais, de exclamacao, de interrogacao e reticencias
	str -> int"""
	return str.count("(texto)",".") + str.count("(texto)","!") + str.count("(texto)","?") + str.count("(texto)","...")