def conta_frases(texto):
    c=texto.count('.')
    c=c+texto.count('!')
    c=c+texto.count('?')
    c=c+texto.count('...')
    return c