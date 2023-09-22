def inverte(frase):
    frase1 = str.lower(frase)
    frase2 = str.replace(frase1, ',' , ' ')
    frase3 = str.replace(frase2, '.' , ' ')
    return frase3