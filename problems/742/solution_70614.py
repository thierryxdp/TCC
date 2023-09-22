def substitui(s,x,i):
    '''Recebe uma string e retorna a mesma string com um caractere diferente. str, str, int -> str.'''
    return s[0:i]+x+s[x+1:]