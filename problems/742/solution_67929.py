def substitui(s,x,i):
    '''Função que substitui blablabla; string,int,int->string'''
    if(i<=len(s)):
        return ((str(s)[:i])+x)+str(s)[i:0]