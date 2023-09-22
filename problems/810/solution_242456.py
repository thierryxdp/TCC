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
    
    frase=(frase[::-1])
    frase=''.join(frase)
    return frase