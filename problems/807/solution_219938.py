def conta_frases(frase):
    if '!' in frase:
        frase = frase.replace('!','.')
    if '?' in frase:
        frase = frase.replace('?','.')
    if '.'*3 in frase:
        frase = frase.replace('.'*3,' ')
    return frase.split('.')