def inverte(frase):
    ''' '''
    frase1=frase.split(' ')
    list.reverse(frase1)
    return str.lstrip(str.lower(str.join(' ',frase1)),' ')