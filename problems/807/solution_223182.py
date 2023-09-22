def conta_frases(frases):
    separar = str.split(frases,'.')
    frases.replace('!','.')
    frases.replace('?','.')
    frases.replace('...','.')
    return len(separar)