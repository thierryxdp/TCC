def conta_frases (texto):
    """Retorna a quantidade de frases dentro de um dado texto.
    Entrada: str
    Saída: int
	"""
    return str.count(texto, '!') + str.count(texto, '?') + str.count(texto, '.') - str.count(texto, '...')*2