def inverte(frase):
    frase= frase.replace(',',' ')
    frase= frase.replace('-',' ')
    frase= frase.replace('.',' ')
    frase= frase.replace(':',' ')
    frase= frase.replace(';',' ')
    frase= frase.replace('?',' ')
    frase= frase.replace('!',' ')
    frase=frase.lower()
    frase=list(frase)
    ''.join(frase)
    
    
    
    return frase[::-1]