def conta_frases(texto):
    """ funcao que calcula o numero de frases de um texto;str,str ->int"""
    x = str.count(texto,'.')  + str.count(texto,'?') + str.count(texto,'!')  
    
    return x