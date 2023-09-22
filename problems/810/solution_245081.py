def inverte(frase):
    '''
    inverte frase sem letras maiusculas e sem pontuacao
    '''
    frase=frase.replace('...',' ')
    frase=frase.replace('-',' ')
    frase=frase.replace('.',' ')
    frase=frase.replace('!',' ')
    frase=frase.replace('?',' ')
    frase=frase.replace(';',' ')
    frase=frase.replace(':',' ')
    frase=frase.replace(',',' ')
    frase=frase.lower()
    frase=frase.count(-1:)
    return frase