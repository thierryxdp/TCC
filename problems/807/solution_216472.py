def conta_frases(frase):
    frase = frase.count('.') + frase.count('?') + frase.count('!')+frase.count('…') + frase.count('...')
    return frase