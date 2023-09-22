def conta_frases(texto):
    l=str.split(texto)
    c=0
    while '!' in l or '.' in l or '?' in l or '...' in l:
    c=c+l.count('.')
    c=c+l.count('!')
    c=c+l.count('?')
    c=c+l.count('...')
    return c