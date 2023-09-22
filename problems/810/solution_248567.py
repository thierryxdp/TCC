def inverte(frase):
    '''
    '''
    frase1=str.split(frase,',')
    frase2=str.split(frase1)
    list.reverse(frase2)
    frase3=str.join(' ',frase2)
    return frase3