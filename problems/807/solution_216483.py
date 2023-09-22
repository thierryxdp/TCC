def conta_frases(frase):
    frase = frase.count('.') + frase.count('?') + frase.count('!')
    frase = str.replace('...','.')
    return frase