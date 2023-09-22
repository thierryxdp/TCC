def conta_frases(texto):
    if '...' in texto:
        c=texto.replace('...','.')
    d=c.count('.')
    d=d+c.count('!')
    d=d+c.count('?')
    return d