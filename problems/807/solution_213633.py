def conta_frases(frases):
    frases = frases.split('.').split('?').split('!').split('...')
    return len(frases)