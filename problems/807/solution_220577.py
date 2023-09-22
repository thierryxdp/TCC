def conta_frases(frase):
    return len(frases.split('!')) + len(frases.split('?'))+len(frases.split('.')) + len(frases.split('...'))