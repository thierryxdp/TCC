def inverte(frase):
    frase  = frase.replace('?',' ')
    frase  = frase.replace('!',' ')
    frase  = frase.replace(',',' ')
    frase  = frase.replace('-',' ')
    frase  = frase.replace(':',' ')
    frase  = frase.replace(';',' ')
    frase  = frase.replace('.',' ')
    frase  = frase.split(' ',frase[-1])
    frase  = frase[-1::-1]
    

    return str.lower(str.join(' ', frase))