def substitui(s,x,i):
    '''
    substitui x da string s em posição i.
    str, str, int -> str
    '''
	b = bytearray(s)
    b[i] = str(x)
    s = str(b)
    return s