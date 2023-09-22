def inverte(frase):
    frase=frase.replace('.',' ')
    frase=frase.replace('!',' ')
    frase=frase.replace(',',' ')
    frase=frase.replace(':',' ')
    frase=frase.replace(';',' ')
    frase=frase.replace('?',' ')
    frase=str.lower(frase)
    frase=(frase[::-1])
    frase=(frase[::-1])
    return frase