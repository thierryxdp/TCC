def conta_frases(x):
    frases = x.count('.')
    frase = x.count('!')
    fras = x.count('...')
    fra = x.count('?')
      if '...' in x:
        return fras + fra + frase
    return frases + frase + fras + fra