def conta_frases(texto):
    str.replace(texto,'...','.')
    f=str.count(texto,'.')+str.count(texto,'?')+str.count(texto,'!')
    return f