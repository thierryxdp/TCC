def conta_frases(frases):
    frases = frases.replace('!','.')
    frases = frases.replace('?','.')
    frases = frases.replace('...','.')
    str.split(frases,'.')
    return len(frases)