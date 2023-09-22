def inverte(frase):
    '''
    funcao inverte a frase e devolve coletras minusculas e sem pontuacao
    '''
    frase=frase.replace('.',' ')
    frase=frase.replace('!',' ')
    frase=frase.replace(',',' ')
    frase=frase.replace(':',' ')
    frase=frase.replace(';',' ')
    frase=frase.replace('?',' ')
    frase=str.lower(frase)
    frase=frase.split()
    frase=(frase)
    frase=frase.replace('[','')
    frase=frase.replace(']','')
    frase=(frase[::-1])
    return frase