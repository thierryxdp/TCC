def conta_frases(texto):
	"""funcao que recebe um texto e retorna o numero de frases inseridas.
		str=>str"""
	ponto = texto.count(".")
	exclamacao = texto.count("!")
	interrogacao = texto.count("?")
	reticencias = texto.count("...")
	pontos = ponto + exclamacao + reticencias + interrogacao
    if reticencias >= 1:
		return pontos - reticencias * 3
	
    return pontos