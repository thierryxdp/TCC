def conta_frases(texto):
    frases=texto.split('!'),texto.split('?'),texto.split('...'),texto.split('!')
    return len(frases)