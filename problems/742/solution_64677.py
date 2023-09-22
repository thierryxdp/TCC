def substitui(s,x,i):
    '''substitui o caractere da posição i da string s
    pelo caractere x'''
    '''string, int, int -> string'''
    s = s[:i] + x + s[i+1:]
    return s