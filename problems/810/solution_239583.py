def inverte(frase):
    frase  = frase.replace('?',' ')
    frase  = frase.replace('!',' ')
    frase  = frase.replace(',',' ')
    frase  = frase.replace('-',' ')
    frase  = frase.replace(':',' ')
    frase  = frase.replace(';',' ')
    frase  = frase.replace('.',' ')
    frase  = frase.split(' ')
    frase  = frase[-1::-1]
    frase  = frase.strip(frase)
    

    return str.lower(str.join(' ', frase))