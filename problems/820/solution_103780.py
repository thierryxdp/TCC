def posLetra(x,l,n):
    '''
    '''
    indices=()
    proximo=0
    while proximo<len(x):
        if x[proximo]==l:
            indices=indices+(proximo,)
        proximo=proximo+1
            
    return indices[n]