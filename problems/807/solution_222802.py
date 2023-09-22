def conta_frases(texto)
	"""
    	Retorna a quantidade de frases que aparecem num texto
        str -> int
    """
    return len(texto.split(['.']['!']['...']['?']))