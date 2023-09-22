def conta_frases(frase):
    frase=frase.replace('!',' ')
    frase=frase.replace('...',' ')
    frase=frase.replace('?',' ')
    frase=frase.replace('.',' ')
    frase=str.split(frase)
    frase=str.join(' ',(frase))
    return frase