def inverte(frase):
    '''
    inverte frase sem letras maiusculas e sem pontuacao
    str -> list
    '''
    frase=frase[0:]
    frase=frase.replace('...',' ')
    frase=frase.replace('-',' ')
    frase=frase.replace('.',' ')
    frase=frase.replace('!',' ')
    frase=frase.replace('?',' ')
    frase=frase.replace(';',' ')
    frase=frase.replace(':',' ')
    frase=frase.replace(',',' ')
    frase=frase.lower()
    frase=frase.reverse()
    return frase
    return frase