def substitui(s,x,i):
    '''recebe um string s, um caractere x e um numero inteiro i entre 0 e o string'''
    c=s
    l= list(c)
    l[i]=x
    return str(c)