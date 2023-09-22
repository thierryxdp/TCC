def conta_frases(texto):
    """..."""
    
    if '...' in texto:
        return 4.replace('...','.')
    else:
        return str.count(texto,'!') + str.count(texto,'?') + str.count(texto,'.')