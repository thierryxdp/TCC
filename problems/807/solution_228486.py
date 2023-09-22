def conta_frases(a,b,c,d):
    '''
    '''    
    
    a=str.split(texto,'.') 
    b=str.split(texto,'?')
    c=str.split(texto,'!')
    d=str.split(texto,'...')
    
    return len(a)+len(b)+len(c)+len(d)