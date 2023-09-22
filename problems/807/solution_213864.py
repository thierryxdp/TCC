def conta_frases(frase):
    f1 = frase.count('.')
    f2 = frase.count('?')
    f3 = frase.count('!')
    f0 = frase.count(frase.replace('...','.'))
    return f0+f1+f2+f3