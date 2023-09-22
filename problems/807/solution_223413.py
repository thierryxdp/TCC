def conta_frases(texto):
    """..."""
    if '...' in texto: 
        return str.strip(texto,'...') 
    else:
        return str.count(texto,'!') + str.count(texto,'?') + str.count(texto,'.')