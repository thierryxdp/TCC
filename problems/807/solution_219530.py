def conta_frases(x):
    frases = x.count('.')
    frase = x.count('!')
    fras = x.count('...')
    fra = x.count('?')
    if '...' in x:
        return frases + frase + fras + fra - fras
    
    return frases + frase + fras + fra