def inverte (frase):
    frase= frase.replace(':', ' ')
    frase= frase.replace('.', ' ')
    frase= frase.replace('-', ' ')
    frase= frase.replace(',', ' ')
    frase= frase.replace('!', ' ')
    frase= frase.replace('?', ' ')
    frase= frase.replace(';', ' ')
    
    frase.casefold()
    
    return frase