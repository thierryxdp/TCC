def conta_frases(texto):
    '''
    str -> int
    '''
    e=str.replace(texto,'!','.')
    i=str.replace(e,'?','.')
    r=str.replace(i,'...','.')
    
    return r