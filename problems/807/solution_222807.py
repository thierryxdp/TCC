def conta_frases(texto):
	"""
    	Retorna a quantidade de frases que aparecem num texto
        str -> int
    """
    texto.replace('!','.')
    texto.replace('...','.')
    texto.replace('?','.')
    return len(texto.split('.'))