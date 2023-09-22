def inverte(frase):
    frase  = frase.replace('?',' ')
    frase  = frase.replace('!',' ')
    frase  = frase.replace(',',' ')
    frase  = frase.replace('-',' ')
    frase  = frase.replace(':',' ')
    frase  = frase.replace(';',' ')
    frase  = frase.replace('.',' ')
    frase  = frase.split(' ')
    frase = frase[-1::0]
    

    return str.lower(str.join(' ', frase))