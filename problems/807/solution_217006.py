def conta_frases(texto):
    str.replace(texto,'...','.')
    str.replace(texto,'?','.')
    str.replace(texto,'!','.')
    return len(str.split(str.split(texto,'.')))