def substitui(s,x,i):
    '''
    string,int,int->string
    '''
    subs=s[0:i]+str(x)+s[i+1:]
    return subs