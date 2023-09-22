def conta_frases(frases):
    return len(frases.split('.')) + len(frases.split('...'))+len(frases.split('?'))+len(frases.split('!'))