def inverte (frase):
    frase = str.lower(frase)
    frase = str.replace(frase, '-', ' ')
    frase = str.replace(frase, '.', ' ')
    frase = str.replace(frase, ':', ' ')
    frase = str.replace(frase, ',', ' ')
    frase = str.replace(frase, ';', ' ')
    frase = str.replace(frase, '!', ' ')
    frase = str.replace(frase, '?', ' ')
    InverteString (frase)
    return frase