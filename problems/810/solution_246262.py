def inverte(frase):
    frase1 = str.lower(frase)
    frase2 = str.replace(frase1, ',' , ' ')
    frase3 = str.replace(frase2, '.' , ' ')
    frase4 = str.replace(frase3, '?' , ' ')
    frase5 = str.replace(frase4, '!' , ' ')
    frase6 = str.replace(frase5, '-' , ' ')
    return frase6