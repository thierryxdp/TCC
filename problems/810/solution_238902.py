def inverte(frase):
    frase = frase.replace('!',' ')
    frase = frase.replace('?',' ')
    frase = frase.replace(',',' ')
    frase = frase.replace('.', ' ')
    frase = frase.replace('-', ' ')
    invertida = (str.split(frase,' '))
    str.join([::-1])
    return invertida