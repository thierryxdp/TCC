def conta_frases (texto):
    """Dado o texto de entrada, retorna o numero de frases do texto. str -> int"""
    return str.count (texto, "." or "!" or "?" or "...")