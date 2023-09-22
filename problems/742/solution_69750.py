def substitui(s,x,i):
    '''Dada uma string s substitui o caractere na posição i por x;
    string, int, int -> string'''
    0 < i < len(s)
    return str(s[0:len(s)-i]) + str(x) + str(s[i+1:])