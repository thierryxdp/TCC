def inverte(x):
    '''inverte uma frase sem sua pontuação'''
    frase=x.replace('-',' ').replace(',',' ').replace(':',' ').replace(';',' ').replace('?',' ').replace('!',' ').replace('.'," ")
    resultado=frase[::-1]
    return resultado