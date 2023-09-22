def inverte (frase):
    str.lower(frase)
    frase= frase.replace(':', ' ')
    frase= frase.replace('.', ' ')
    frase= frase.replace('-', ' ')
    frase= frase.replace(',', ' ')
    frase= frase.replace('!', ' ')
    frase= frase.replace('?', ' ')
    frase= frase.replace(';', ' ')
    
    return frase