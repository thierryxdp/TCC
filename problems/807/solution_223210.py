def conta_frases(texto):
    """..."""
    
    
    
    if ('...'=1) in texto:
        return str.count(texto,'!') + str.count(texto,'?') + str.count(texto,'...') + str.count(texto,'.') - int(3)
    else:
        return str.count(texto,'!') + str.count(texto,'?') + str.count(texto,'.')