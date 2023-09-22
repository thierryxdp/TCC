def inverte(frase):
    frase  = frase.replace('?',' ')
    frase  = frase.replace('!',' ')
    frase  = frase.replace(',',' ')
    frase  = frase.replace('-',' ')
    frase  = frase.replace(':',' ')
    frase  = frase.replace(';',' ')
    frase  = frase.replace('.',' ')
    frase  = frase.split(' ',-1)
    frase  = frase[-1::-1]
    

    return str.lower(str.join(' ', frase))