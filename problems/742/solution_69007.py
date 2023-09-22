def substitui(s,x,i):
    '''
    string,int,int->string
    '''
    subs=[0:i]+str(x)+s[i+1:]
    return subs