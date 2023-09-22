def substitui(s,x,i):
    '''
    Substitui o caractere na posição i de uma string s por um caractere x.
    str, str, int -> str
    '''
    return s[0:i]+x+s[i+1,]