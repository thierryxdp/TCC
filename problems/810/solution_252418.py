def inverte(frase):
    '''inverte a ordem das palavras de uma frase
    str-->str'''
    a=str.replace(frase,',',' ')
    b=str.split(a)
    list.reverse(b)
    c=str.join(' ',b)
    return c