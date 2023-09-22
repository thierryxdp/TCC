def substitui(s,x,i):
    '''Troca o caractere X na posição I. 
    string, int, int -> string'''
    s = list(s)
    s[i] = x
    s = ''.join(s)
    return str(s)