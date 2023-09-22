def conta_frases(frases):
    a = frases.count('...')
    b = frases.count('!')
    d = frases.count('?')
    A = a + b + d
    return A