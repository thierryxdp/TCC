def conta_frases(texto):
    frases = str.count(texto,'!')+ str.count(texto,'?')+ str.count(texto,'...')
    resultado = frases + str.count(texto,'.')- str.count(texto,'...')
    return resultado