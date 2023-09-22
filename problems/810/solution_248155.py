def inverte (frase):
    ''' retorna o inverso da frase dada'''
    frase = list.remove (frase , '.')
    frase = list.remove (frase , ',')
    frase = list.lower (frase)
    return list.reverse(frase)