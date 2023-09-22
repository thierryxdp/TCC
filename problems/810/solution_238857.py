def inverte(frase):
    frase = frase.replace('!',' ')
    frase = frase.replace('?',' ')
    frase = frase.replace(',',' ')
    frase = frase.replace('.', ' ')
    frase = frase.replace('-', ' ')
    for palavra in frase.split(" "):
        frase += palavra[::-1]+" "
        return frase