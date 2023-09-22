def inverte(frase):
    """"""
    frase1=str.split(frase, '-')
    frase2=str.split(frase1, ',')
    frase3=str.split(frase2, ':')
    frase4=str.split(frase3, ';')
    frase5=str.split(frase4, '...')
    frase6=str.split(frase5, '?')
    frase7=str.split(frase6, '!')
    frase8=str.split(frase7, '.')
    frase9=str.lower(frase8)
    frase10=frase9.reverse()
    return frase10