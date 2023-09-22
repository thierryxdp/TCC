def inverte(frase):
    frase = frase.replace('.',' ')
    frase = frase.replace('!',' ')
    frase = frase.replace('?',' ')
    frase = frase.replace(',',' ')
    frase = frase.replace('-',' ')
    frase = frase.replace(':',' ')
    frase = frase.replace(';',' ')
    frase = frase.lower()
    frase.reverse()
    
    return frase