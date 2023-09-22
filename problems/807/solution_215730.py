def conta_frases(texto):
    """Retorna o número de frases de um texto dado; str -> int"""
    x = [".","...","!","?"]
    return str.count(texto,x)