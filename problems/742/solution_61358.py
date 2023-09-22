def substitui(s,x,i):
    '''substitui um elemento da posição i da string s pelo caractere x
    string,string,int -> string'''
    index = s[i]
    if index in (len(s)-1):
        index == x
        return s