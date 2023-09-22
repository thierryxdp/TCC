def conta_frases(frases):
    frases = frases.replace('!','.')
    frases = frases.replace('?','.')
    frases = frases.replace('...','.')
    frases.split('.')
    return len(frases)