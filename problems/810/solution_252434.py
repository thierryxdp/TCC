def inverte(frase):
    '''inverte a ordem das palavras de uma frase
    str-->str'''
    a=str.lower(frase)
    a=str.replace(a,',',' ')
    a=str.replace(a,'?',' ')
    a=str.split(b)
    list.reverse(c)
    a=str.join(' ',c)
    return a