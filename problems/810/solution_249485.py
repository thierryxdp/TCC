def inverte(frase):
    frase = frase.replace('.',' ').replace(',',' ').replace('-',' ').replace('?',' ').replace('!',' ')
    frase = frase.split()
    return frase[::-1]