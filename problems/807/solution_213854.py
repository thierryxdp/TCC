def conta_frases(frase):
    f0 = frase.replace('...','.')
    f1 = frase.count('.')
    f2 = frase.count('?')
    f3 = frase.count('!')

    return f1+f2+f3+f4