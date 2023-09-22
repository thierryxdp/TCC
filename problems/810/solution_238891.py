def inverte(frase):
    frase = frase.replace('!',' ')
    frase = frase.replace('?',' ')
    frase = frase.replace(',',' ')
    frase = frase.replace('.', ' ')
    frase = frase.replace('-', ' ')
    invertida = (str.split(frase,''))
    return invertida