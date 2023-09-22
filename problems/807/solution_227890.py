def conta_frases(frase):
    frase.replace('...','.')
    return frase.count('.')  + frase.count('!') +frase.count('?')