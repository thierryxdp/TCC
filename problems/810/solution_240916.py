def inverte (frase):
    frase=frase.replace('.',' ')
    frase=frase.replace('?',' ')
    frase=frase.replace(',',' ')
    frase=frase.replace('!',' ')
    frase=frase.replace('-',' ')
    frase=str.lower(frase)
    frase=frase.split(frase)
    return frase[::-1]