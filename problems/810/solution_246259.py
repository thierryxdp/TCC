def inverte(frase):
    frase1 = str.lower(frase)
    frase2 = str.replace(frase1, ',' , ' ')
    frase3 = str.replace(frase2, '.' , ' ')
    frase4 = str.replace(frase3, '?' , ' ')
    return frase4