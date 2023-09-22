def substitui(s,x,i):
    '''
       Função que;
       string, int, int -> string
    '''
    sub = s[0:i]+x+s[i-1:]
    return sub