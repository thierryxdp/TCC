def conta_frases(x):
    frases = x.count('...')
    fras = x.count('.')
    frase = x.count('!')
    fra = x.count('?')
    fr = -1*(fras - (frases * 3))
    if '...' in x:
        return frases + frase + fra + fras - fr
    return frases + frase + fra + fras