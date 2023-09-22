def conta_frases(texto):
    """..."""
    
    if '...' in texto:
        return str.replace('...','.',1)
    else:
        return str.count(texto,'!') + str.count(texto,'?') + str.count(texto,'.')