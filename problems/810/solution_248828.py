def inverte(frase):

    for dado in '-.,':

        frase = frase.replace(dado, '')
    
    frase = frase[::-1]

    return frase