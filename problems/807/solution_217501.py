def conta_frases(texto):
    str.replace(texto,'?','.')
    str.replace(texto,'!','.')
    str.replace(texto,'...','.')
    f=str.count(texto,'.')
    return f