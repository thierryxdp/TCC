def inverte(frase):
    frase = frase.replace('-',' ')
    frase = frase.replace(',',' ')
    frase = frase.replace(':',' ')
    frase = frase.replace('.',' ')
    frase = frase.replace('!',' ')
    frase = frase.replace('?',' ')
    
    frases = str.split(frase,' ', -1)
    
    return str.join(' ',frases)