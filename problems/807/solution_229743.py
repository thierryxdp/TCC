def conta_frases(c):
    '''
    
    '''
    x=str.count(c,'!')
    y=str.count(c,'?')
    w=str.count(c,'.')
    v=str.count(c,'...')
    h=v-(3*v)
    return x+y+w+h