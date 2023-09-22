def inverte(frase):
    frase = frase.replace(',',' ')
    frase = frase.replace('!',' ')
    frase = frase.replace('.',' ')
    frase = frase.replace('?',' ')
    frase = frase.replace('-',' ')
    frase = frase.split(frase,' ')
    return frase