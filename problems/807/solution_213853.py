def conta_frases(frase):
    
    f1 = frase.count('.')
    f2 = frase.count('?')
    f3 = frase.count('!')
    f4 = frase.replace('...','.')
    return f1+f2+f3+f4