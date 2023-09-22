def conta_frases(texto):
    """..."""
    
    
    if str.replace("texto","...",".",4) in texto:
        return str.count(texto,'!') + str.count(texto,'?') + str.count(texto,'...') + str.count(texto,'.') 
    else:
        return str.count(texto,'!') + str.count(texto,'?') + str.count(texto,'.')