def substitui(s,x,i):
    '''Uma função que substitui uma letra x de uma string s, em uma posição i.
    str, int, int -> string'''
    return s[0:i]+x+s[-1:i]