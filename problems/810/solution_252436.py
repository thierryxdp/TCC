def inverte(frase):
    '''inverte a ordem das palavras de uma frase
    str-->str'''
    a=str.lower(frase)
    a=str.replace(a,',',' ')
    a=str.replace(a,'?',' ')
    a=str.split(a)
    list.reverse(a)
    a=str.join(' ',a)
    return a