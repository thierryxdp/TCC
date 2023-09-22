def conta_frases(texto):
    f=str.count(texto,'.')+str.count(texto,'...')+str.count(texto,'?')+str.count(texto,'!')
    return f