def inverte(frase):
    
    frase=frase.replace('-',' ')
    frase=frase.replace(',',' ')
    frase=frase.replace(':',' ')
    frase=frase.replace(';',' ')
    frase=frase.replace('.',' ')
    frase=frase.replace('!',' ')
    frase=frase.replace('?',' ')
    
    frase=str.lower(frase)
    
    return list.sort([frase], reverse=True)