# string, int, int -> string
def substitui(s,x,i):
    '''função que substitui uma caractere da posição i pelo caractere x'''
    0<i<=len(s)
    s = s[:i] + x + s[i+1:]
    return s