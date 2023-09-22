def conta_frases(texto):
    """ """
    x = str.count(texto,'.') + str.count(texto,'?') + str.count(texto,'!')  
    if '...' in 'texto':        
        return x + 2
    else:
        return x