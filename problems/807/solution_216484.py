def conta_frases(frase):
    frase = frase.count('.') + frase.count('?') + frase.count('!')
    frase = str.replace(frase,'...','.')
    return frase