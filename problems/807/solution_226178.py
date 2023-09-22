def conta_frases(texto):
    """Retorna o número de frases de um determinado texto.
    str -> int"""
    return str.slpit(str.replace(str.replace(str.replace(texto,"!","."),"?","."),"...","."))