def substitui(s,x,i):
    ''' retorna uma string s onde o elemento da posiçao i é substituido pelo caractere x'''
    '''str, int, int -> str'''
    s[i] = x
    s[0:i] + x + s[i:]
    return s