def inverte(frase):
    '''str --> str'''
    frase = str.lower(frase)
    frase_dividida = str.split(frase)
    frase_invertida = frase_dividida[::-1]
    return frase_invertida