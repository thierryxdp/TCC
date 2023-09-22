def conta_frases(frases):
    a = frases.count('...')
    b = frases.count('!')
    c = frases.count('?')
    d = frases.count('.')
    A = a + b + c
    if '...' not in frases:
        return A
    else:
        return A - (3*frases.count('...'))