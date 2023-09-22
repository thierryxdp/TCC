def inverte (frase):
    frase.lower()
    
    frase= frase.replace(':', ' ')
    frase= frase.replace('.', ' ')
    frase= frase.replace('-', ' ')
    frase= frase.replace(',', ' ')
    frase= frase.replace('!', ' ')
    frase= frase.replace('?', ' ')
    frase= frase.replace(';', ' ')
    
    lista = frase.split(' ')
    
    lista = sorted(lista, reverse=True)
    
    inver = ' '.join(lista)
    
    return inver