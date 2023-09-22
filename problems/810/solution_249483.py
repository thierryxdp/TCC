def inverte(frase):
    frase = frase.replace('.',' ').replace(',',' ').replace('-',' ').replace('?',' ').replace('!',' ')
    return frase[::-1]