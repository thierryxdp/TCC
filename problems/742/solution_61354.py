def substitui(s,x,i):
    '''substitui um elemento da posição i da string s pelo caractere x
    string,string,int -> string'''
    if i in len(s):
        s[i] = x
        return s