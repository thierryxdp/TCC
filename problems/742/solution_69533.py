def substitui(s,x,i):
    '''funcao que substitui os valores de lugares na funcao
    str,int,int->int'''
    a=s
    b=x
    c=(i==x)
    return str(a[:1]),b,c[i+1:]