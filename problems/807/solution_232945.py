def conta_frases(texto):
    l=str.split(texto)
    c=l.count('.')
    c=c+l.count('!')
    c=c+l.count('?')
    c=c+l.count('...')
    return c