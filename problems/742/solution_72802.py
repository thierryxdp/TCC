def substitui(s,x,i):
    '''string, int, int -> string'''
    s[i]=x
    return s[0:i] + x + s[i + 1:]