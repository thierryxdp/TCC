def conta_frases(texto):
    """..."""
    
    ... = 1
    
    if '...' in texto:
        return str.count(texto,'!') + str.count(texto,'?') + str.count(texto,'...') + str.count(texto,'.') - int(3)
    else:
        return str.count(texto,'!') + str.count(texto,'?') + str.count(texto,'.')