def inverte(frase):
    '''
    '''
    
    frase2=str.split(frase,',')
    list.reverse(frase2)
    frase3=str.join(' ',frase2)
    return frase3