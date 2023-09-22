def conta_frases(frase):
    if frase.replace('...','.'):
        return '.'
    return frase.count('.')  + frase.count('!') +frase.count('?')