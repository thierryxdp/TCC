def inverte(frase):
    frase = frase.replace(',',' ')
    frase = frase.replace('-',' ')
    frase = frase.replace(':',' ')
    frase = frase.replace(';',' ')
    frase = frase.replace('.',' ')
    frase = frase.replace('?',' ')
    frase = frase.replace('!',' ')
    separa = frase.split(' ')
    separa = separa[::-1]
    return (((',' .join(separa)).replace( [',',' ')).lower())