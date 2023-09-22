def conta_frases(texto):
    """..."""
    
    if '...' in texto:
        return str.replace('...','...','4')
    else:
        return str.count(texto,'!') + str.count(texto,'?') + str.count(texto,'.')