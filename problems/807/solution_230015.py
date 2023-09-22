def conta_frases(frase):
    if '...' in frase:
        frase = frase.replace('...','.')
    
    a= frase.count('.')
    b = frase.count('?')
    c = frase.count('!')

    return a+b+c