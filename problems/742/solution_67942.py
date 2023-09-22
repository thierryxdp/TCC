def substitui(s,x,i):
    '''Função que substitui o elemento de índice i por x na string s; string,int,int->string'''
    if(i<=len(s)):
        return ((str(s)[:i])+x)+str(s)[-1:-i]