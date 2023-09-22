def conta_frases(frase):
    frase=frase.replace('!',' ')
    frase=frase.replace('...',' ')
    frase=frase.replace('?',' ')
    frase=frase.replace('.',' ')
    frase=str.split(frase)
    return frase