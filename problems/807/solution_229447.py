def conta_frases(x):
    '''
    '''
    k=str.count(x,'...')
    b=str.count(x,'.')
    c=str.count(x,'!')
    v=str.count(x,'?')
    n=str.count(x,'...')
    
    return (k+b+c+v+n)