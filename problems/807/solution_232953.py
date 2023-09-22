def conta_frases(texto):
    a='...'
    c=texto.count('.')
    c=c+texto.count('!')
    c=c+texto.count('?')
    c=c+texto.count(a)
    return c