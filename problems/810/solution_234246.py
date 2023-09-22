def inverte(frase):
    frase = frase.replace(',',' ')
    frase = frase.replace('!',' ')
    frase = frase.replace('.',' ')
    frase = frase.replace('?',' ')
    frase = frase.replace('-',' ')
    frase = str.split(frase)
    frase = frase[::-1]
    frase = str.join(' ',(frase))
    return frase