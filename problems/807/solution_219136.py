def conta_frases(texto):
    texto = str.count(texto,'!')+ str.count(texto,'?') 
    + str.count(texto,'...') + str.count(texto,'.')
    return texto