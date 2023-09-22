def substitui(s,x,i):
    '''dados a string, o caractere e a posição, substitui o elemento na posição i de uma string s por um caractere x
    string, int, int -> string'''
    novo = s[:i] + x + s[i:]
    return novo