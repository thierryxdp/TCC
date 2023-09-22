def inverte (frase):
    frase: frase.replace(':', ' ')
    frase: frase.replace('.', ' ')
    frase: frase.replace('-', ' ')
    frase: frase.replace(',', ' ')
    frase: frase.replace('!', ' ')
    frase: frase.replace('?', ' ')
    frase: frase.replace(';', ' ')

    frase.lower()
    
    return frase