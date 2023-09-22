def conta_frases(x):
    frases = x.count('...')
    fras = x.count('.')
    frase = x.count('!')
    fra = x.count('?')
    if '...' in x and '.' in x:
        return frases + frase + fra + fras - (frases * 2)
    return frases + frase + fra + fras