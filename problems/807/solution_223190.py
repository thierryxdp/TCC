def conta_frases(frases):
    frases.replace('!','.').replace('?','.').replace('...','.')
    separar = str.split(frases,'.')
    return len(separar)