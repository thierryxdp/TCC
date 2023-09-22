def conta_frases(frase):
    a = '...'
    b = '.'
    return frase.count(b) + frase.count('!') + frase.count('?') + frase.count(a)