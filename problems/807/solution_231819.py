def conta_frases(texto):
    """Retorna o número de frases em um texto
    assinatura: str -> int"""
    separador = ['.', '!', '?', '...']
    for x in separador:
    	return len(str.split(texto, x))