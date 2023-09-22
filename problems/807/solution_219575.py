def conta_frases(x):
    frases = x.count('...')
    fras = x.count('.')
    frase = x.count('!')
    fra = x.count('?')
    fr = frases + fras
    if '...' in x:
        return frases + frase + fra + fras - fr
    return frases + frase + fra + fras