def conta_frases(frases):
    a = frases.count('...')
    b = frases.count('!')
    c = frases.count('?')
    A = a + b + c
    frases.replace('...', ' ')
    d = frases.count('.')
    A = A + d
    return A