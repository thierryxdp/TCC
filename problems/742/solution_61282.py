def substitui(s,x,i):
    ''' função que substitui o elemento de posição i pelo caractere x na string s;
    string,int,int->string'''
    z=i+1
    return s[:i]+x+s[z:]