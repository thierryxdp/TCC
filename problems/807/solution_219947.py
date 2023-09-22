def conta_frases(frase):
    if '!' in frase:
        frase = frase.replace('!',',')
    if '?' in frase:
        frase = frase.replace('?',',')
    if ';' in frase:
        frase = frase.replace(';',',')
    return frase.split(',')