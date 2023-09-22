def substitui(s,x,i):
    ''' substitui um elemento na posição i pelo caractere x
str,str,int->str'''
    s= s[0:i]+str(x)+s[i+1:]
    return s