def inverte(frase):    
    """função que retorna a frase de entrada ao contrário, sem as pontuações gramaticais e sem letras maiusculas
    str --> str"""
    frase = frase.replace('.','')
    frase = frase.replace('...','')
    frase = frase.replace('?','')
    frase = frase.replace('!','')
    frase = frase.replace('-','')
    frase = frase.replace('_','')
    frase = frase.replace(';','')
    frase = frase.replace(':','')
    frase = frase.replace(',','')
    frase = frase.lower()
    frase = frase.split(' ')
    frase = frase[::-1]
    frase = ' '.join(frase)
    return frase