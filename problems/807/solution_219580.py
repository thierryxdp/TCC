def conta_frases(x):
    frases = x.count('...')
    fras = x.count('.')
    frase = x.count('!')
    fra = x.count('?')
    if '...' in x and '.' in x:
        return frases + frase + fra + fras - fras + frases
    return frases + frase + fra + fras