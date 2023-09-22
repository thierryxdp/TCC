def inverte (frase):
    frase= frase.replace(':', ' ')
    frase= frase.replace('.', ' ')
    frase= frase.replace('-', ' ')
    frase= frase.replace(',', ' ')
    frase= frase.replace('!', ' ')
    frase= frase.replace('?', ' ')
    frase= frase.replace(';', ' ')
    
    frase = frase.lower()
    
    lista = frase.split(' ')
    
    lista = sorted(lista, reverse = True)
    
    inver = ' '.join(lista)
    
    return inver