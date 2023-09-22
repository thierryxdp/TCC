def conta_frases(texto):
    if '...' in texto:
        texto.replace('...','.')
    c=texto.count('.')
    c=c+texto.count('!')
    c=c+texto.count('?')
    return c