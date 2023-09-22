def substitui(s,x,i):
    '''substitui um elemento da posição i da string s pelo caractere x
    string,string,int -> string'''
    n == s[0:i-1] + x + s[i+1:]
    return n