def inverte(frase):
    frase = frase.replace('!',' ')
    frase = frase.replace('?',' ')
    frase = frase.replace(',',' ')
    frase = frase.replace('.', ' ')
    frase = frase.replace('-', ' ')
    for palavra in frase.split(" "):
        invertida += palavra[::-1]+" "
        return invertida