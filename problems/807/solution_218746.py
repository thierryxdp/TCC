def conta_frases(texto):
    """ """
    x = str.count(texto,'.')//str.count(texto,'.') + str.count(texto,'?') + str.count(texto,'!')  
    if '...' in x:
        
        return x - 2
    else:
        x