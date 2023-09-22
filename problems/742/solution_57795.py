def substitui(s,x,i):
    '''Função que, dada uma string s, um caractere x e um inteiro i, retorna a string s com a posição i substituida pelo caractere x.
    string, int, int -> string'''
    return s[0:i] + x + s[(i+1):]