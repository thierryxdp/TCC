def inverte (frase):
    frase=frase.replace('.',' ')
    frase=frase.replace('?',' ')
    frase=frase.replace(',',' ')
    frase=frase.replace('!',' ')
    frase=frase.replace('-',' ')
    frase=str.lower(frase)
    return ''.join(inverte(frase[::-1])