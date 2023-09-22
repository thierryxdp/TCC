def conta_frases(texto):
    texto=str.replace(texto,'...','.')
    texto=str.replace(texto,'?','.')
    texto=str.replace(texto,'!','.')
    texto=str.split(texto,'.')
    return len(texto)-1