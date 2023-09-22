def conta_frases(frases):
    frases.replace('!','.')
    frases.replace('?','.')
    frases.replace('...','.')
    separar = str.split(frases,'.')
    return len(separar)