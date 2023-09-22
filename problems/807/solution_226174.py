def conta_frases(texto):
    """Retorna o número de frases de um determinado texto.
    str -> int"""
    return len(str.split(str.strip((texto),";",","),"."))