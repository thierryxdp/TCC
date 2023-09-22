def conta_frases(texto):
    frases=texto.split('!'),texto.split('?'),texto.split('...'),texto.split('.')
    print (frases)
    return len(frases)