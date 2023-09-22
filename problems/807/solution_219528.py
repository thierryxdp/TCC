def conta_frases(x):
    frases = x.count('.')
    frase = x.count('!')
    fras = x.count('...')
    fra = x.count('?')
    
    return frases + frase + fras + fra