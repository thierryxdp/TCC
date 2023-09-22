def inverte(frase):
    '''
    '''
    frase1=str.split(frase,',')
    frase2=str.split(frase)
    list.reverse(frase2)
    frase3=str.join(' ',frase2)
    return frase3