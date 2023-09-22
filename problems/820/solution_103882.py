def posLetra(x,l,n):
    '''
    '''
    if str.count(x,l)<n:
        return -1
    
    indices=()
    proximo=0
    
    while proximo<len(x):
        if x[proximo]==l:
            indices=indices+(proximo,)
        proximo=proximo+1
        
    return indices[n-1]