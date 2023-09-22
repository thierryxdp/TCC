def conta_frases(x):
    frases = x.count('.')
    frase = x.count('!')
    fras = x.count('...')
    fra = x.count('?')
    fr = frases - fras * 3
    if '...' in x:
        return frase + fras + fra - fr
    return frases + frase + fras + fra