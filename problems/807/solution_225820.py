def conta_frases (texto):
    """Dado um texto, retorna seu número de frases. str -> int"""
    return len (str.split(texto, ('.' or'!' or '?' or '...')))