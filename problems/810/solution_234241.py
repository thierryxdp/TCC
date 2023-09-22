def inverte(frase):
    frase = frase.replace(',',' ')
    frase = frase.replace('!',' ')
    frase = frase.replace('.',' ')
    frase = frase.replace('?',' ')
    frase = frase.replace('-',' ')
    frase = str.split(frase)
    frase = str.join(' ',(frase))
    frase = frase[::1]
    return frase