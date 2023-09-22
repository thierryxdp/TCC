def inverte(frase):
    
    frase=frase.replace('-',' ')
    frase=frase.replace(',',' ')
    frase=frase.replace(':',' ')
    frase=frase.replace(';',' ')
    frase=frase.replace('.',' ')
    frase=frase.replace('!',' ')
    frase=frase.replace('?',' ')
    
    frase=str.lower(frase)
    
    list.reverse(frase)
    
    frase=frase.replace(',',' ')
    
    return frase