def substitui(s,x,i):
    '''substitui o caracter i pelo caracter x em uma determinada string.'''
    0 >= i <= len(s)
    return s[:i] + str(x) + s[i+1:]