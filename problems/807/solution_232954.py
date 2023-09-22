def conta_frases(texto):
    a='...'
    b='.'
    c=texto.count(b)
    c=c+texto.count('!')
    c=c+texto.count('?')
    c=c+texto.count(a)
    return c