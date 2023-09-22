def conta_frases(texto):
    """..."""
    if '...' in texto: 
        return texto.count(str.strip(texto,'...')) + str.count(texto, '?') + str.count(texto, '!') + str.count(texto, '.')
    else:
        return str.count(texto,'!') + str.count(texto,'?') + str.count(texto,'.')