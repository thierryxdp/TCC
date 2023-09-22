def substitui(s,x,i):
    """substitui o elemento [i] da string s pelo x
    str,str,int-str"""
    M = str(s)[0:i]
    N = str(s)[(i+1):-1]
    O = M + str(x) + N
    return O