def conta_frases(texto):
    frases = str.count(texto,'!')+ str.count(texto,'.')+ str.count(texto,'?')+ str.count(texto,'...')
    return frases