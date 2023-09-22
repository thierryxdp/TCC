def conta_frases(texto):
    '''
    '''    
    
    a=str.split(texto,'.') 
    b=str.split(texto,'?')
    c=str.split(texto,'!')
    d=str.split(texto,'...')
    
    return len(a,b,c,d)