def conta_frases(texto):
    """calcula e retorna o número de frases em um texto"""
    return str.count(texto,"." or "!" or "?" or "...")