def inverte(frase):
    frase = frase.replace(',',' ')
    frase = frase.replace('!',' ')
    frase = frase.replace('.',' ')
    frase = frase.replace('?',' ')
    frase = frase.replace('-',' ')
    frase = str.split(frase)
    return frase