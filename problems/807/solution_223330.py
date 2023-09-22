def conta_frases(texto):
    """..."""
    
    if '...' in texto:
        return 4
    else:
        return str.count(texto,'!') + str.count(texto,'?') + str.count(texto,'.')