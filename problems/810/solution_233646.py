def inverte (frase):
    frase = str.lower()
    frase = str.replace(frase, '-', ' ')
    frase = str.replace(frase, '.', ' ')
    frase = str.replace(frase, ':', ' ')
    frase = str.replace(frase, ',', ' ')
    frase = str.replace(frase, ';', ' ')
    frase = str.replace(frase, '!', ' ')
    frase = str.replace(frase, '?', ' ')
    return frase