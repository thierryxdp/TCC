def substitui(s,x,i):
    '''A função substitui um local indicado da frase
    string, int, int -> string'''
    
    y = list(s)
    y[i] = x
    z = "".join(y)
    
    return z