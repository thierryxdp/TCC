def conta_frases(frases):
    str.replace(frases,'!','.')
    str.replace(frases,'?','.')
    str.replace(frases,'...','.')
    separar = str.split(frases,'.')
    return len(separar)