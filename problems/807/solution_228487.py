def conta_frases(texto):
    '''
    '''    
    
    a=str.split(texto,'.') 
    b=str.split(texto,'?')
    c=str.split(texto,'!')
    d=str.split(texto,'...')
    
    
    texto=a+b+c+d  
    
    return len(texto)