def conta_frases(texto):
    """..."""
    
    if str.replace("texto","...",".") in texto:
        return str.count(texto,'!') + str.count(texto,'?') + str.count(texto,'...') + str.count(texto,'.') - int(2)
    else:
        return str.count(texto,'!') + str.count(texto,'?') + str.count(texto,'.')