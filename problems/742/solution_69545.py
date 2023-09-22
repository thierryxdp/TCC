def substitui(s,x,i):
    '''funcao que substitui os valores de lugares na funcao
    str,int,int->int'''
    return s[:i]+str(x)+s[i+1:]