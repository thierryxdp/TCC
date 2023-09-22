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
    

    return str.strip(str.lower(str.join('', frase)))