def substitui(s,x,i):
    '''Substitui determinado elemento, numa posição (i) de 
    uma string (s) por um caractere (x).
    string, int, int -> string'''
    return s[0:i]+x+s[(i+1): ]