def conta_frases(frase):
    frase = str.replace(frase,'...','.')
    frase = frase.count('.') + frase.count('?') + frase.count('!') + frase.count('..') + frase.count('…')
    return frase