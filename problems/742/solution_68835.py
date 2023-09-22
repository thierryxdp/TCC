def substitui(s,x,i):
    ''' retorna s substituindo i por x'''
    '''str,int,int-> str'''
    return s[:i]+str(x)+s[i+1:]