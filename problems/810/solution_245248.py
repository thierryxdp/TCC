def inverte(frase):
    '''
    dada uma frase, a retorna sem letras maiusculas, pontuacoes e de trás para frente
    str -> list
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
    frase=list(frase)
    frase=frase.reversed()
    return frase