def inverte (frase):
    ''' retorna o inverso da frase dada'''
    frase = str.replace (frase , '.', '')
    frase = str.replace (frase , ',', '')
    frase = str.lower (frase)
    return frase[::-1]