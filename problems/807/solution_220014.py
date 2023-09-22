def conta_frases(frase):
    "Conta o número de frases que aparecem neste texto."
    frase = frase.replace('!','.')
    frase = frase.replace('?','.')
    frase = frase.replace('...','.')
    frase = frase.split('.')
    frase = len(frase)
    return frase