def conta_frases(frase):
    if '!' in frase:
        frase = frase.replace('!','-')
    if '?' in frase:
        frase = frase.replace('?','-')
    if '.'*3 in frase:
        frase = frase.replace('.'*3,' ')
    if '. ' in frase:
        frase = frase.replace('. ','-')
    return frase.split('-')