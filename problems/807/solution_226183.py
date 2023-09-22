def conta_frases(texto):
    """Retorna o número de frases de um determinado texto.
    str -> int"""
    a = str.replace(str.replace(str.replace(texto,"!","."),"?","."),"...","."),".")
    return str.slpit(a,)