def inverte(frase):
    frase = frase.replace('-',' ')
    frase = frase.replace(',',' ')
    frase = frase.replace(':',' ')
    frase = frase.replace('.',' ')
    frase = frase.replace('!',' ')
    frase = frase.replace('?',' ')
    
    frases = frase.split(frase,' ',-1)
    
    return frases.join('',frases)