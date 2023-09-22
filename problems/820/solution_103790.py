def posLetra(x,l,n):
    '''
    '''
    if str.count(x,l)<n:
        return -1
    
    y=()
    w=0
    
    while w<len(x):
        if x[w]==l:
            y=y+(w,)
        w=w+1
        
    return y[n-1]