def inverte(frase):
    frase = frase.replace('.',' ')
    frase = frase.replace('!',' ')
    frase = frase.replace('?',' ')
    frase = frase.replace(',',' ')
    frase = frase.replace('-',' ')
    frase = frase.replace(':',' ')
    frase = frase.replace(';',' ')
    frase = frase.lower()
    return frase