def conta_frases(x):
    frases = x.count('...')
    fras = x.count('.')
    frase = x.count('!')
    fra = x.count('?')
    if '...' in x:
        return frases + frase + fra + fras - (frases * 3)
    return frases + frase + fra + fras