def conta_frases(frase):
    f1 = frase.count(frase.replace('...','.'))
    f2 = frase.count('?')
    f3 = frase.count('!')

    return f1+f2+f3