def inverte (frase):
    ''' retorna o inverso da frase dada'''
    frase = str.remove (frase , '.')
    frase = str.remove (frase , ',')
    frase = str.lower (frase)
    return str.reverse(frase)