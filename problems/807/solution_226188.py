def conta_frases(texto):
    """Retorna o número de frases de um determinado texto.
    str -> int"""
    texto = str.replace(str.replace(str.replace(texto,"!","."),"?","."),"...",".")
    return len(str.split(texto,))