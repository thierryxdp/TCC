def inverte(string):
    '''retorna o parametro de entrada em ordem inversa, sem pontos; str->str'''
    x=str.lower(string)
    x=str.replace(x,'.','')
    x=str.replace(x,',','')
    x=str.replace(x,'!','')
    x=str.replace(x,'?','')
    x=str.replace(x,'-',' ')
    x=str.split(x)
    list.reverse(x)
    x=str.join(' ',x)
    return x