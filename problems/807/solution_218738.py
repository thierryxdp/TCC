def conta_frases(texto):
    """ """
    x = int(str.count(texto,'.'))//int(str.count(texto,'.')) + str.count(texto,'?') + str.count(texto,'!')  
    
    return x