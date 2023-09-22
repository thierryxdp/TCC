def conta_frases(frase):
    if frase :
        return frase.replace('...','.')
    elif frase:
        return frase.count('.')  + frase.count('!') +frase.count('?')