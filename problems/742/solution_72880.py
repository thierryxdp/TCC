def substitui(s,x,i):
    '''string, int, int -> string'''
    l=list(s)
    l[i]=x
    return (s[0:i]+x+s[i+1:])