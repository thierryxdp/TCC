def conta_frases(texto):
    """..."""
    
    
    
    if '...' in texto:
        return str.count(texto,'!') + str.count(texto,'?') + str.count(texto,'...') + str.count(texto,'.') - int(3)
    else:
        return str.count(texto,'!') + str.count(texto,'?') + str.count(texto,'.')