def conta_frases (frase):
    frase=frase.replace('!','t')
    frase=frase.replace('?','t')
    frase=frase.replace('.','t')
    frase=frase.replace('...','t')
    return frase