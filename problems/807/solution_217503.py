def conta_frases(texto):
    str.replace(texto,'?','.')
    str.replace(texto,'!','.')
    str.replace(texto,'...','.')
    str.split(texto,'.')
    return len(texto)-1