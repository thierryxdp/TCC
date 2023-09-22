def conta_frases(x):
    frases = x.count('.')
    frase = x.count('!')
    fras = x.count('...')
    fra = x.count('?')
    if '...' in x and '.' in x:
        return frase + fras + fra
    return frases + frase + fras + fra