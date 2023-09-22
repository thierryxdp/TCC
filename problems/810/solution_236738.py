def inverte (frase):
    frase: frase.replace(':', ' ')
    frase: frase.replace('.', ' ')
    frase: frase.replace('-', ' ')
    frase: frase.replace(',', ' ')
    frase: frase.replace('!', ' ')
    frase: frase.replace('?', ' ')
    frase: frase.replace(';', ' ')
    frase: frase.replace('...', ' ')
    
    frase.lower()
    
    lista = frase.split(' ')
    
    lista = lista[::-1]
    
    inver= ' '.join(lista)
    
    return inver