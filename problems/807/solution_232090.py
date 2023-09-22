def conta_frases(x):
    
    retcs=x.count('...')
    if retcs>0:
        rects=x.count('...')-3
    
    interrog=x.count('?')
    exc=x.count('!')
    ponto=x.count('.')
  
    
        
    x=retcs+interrog+exc+ponto
    
    
    
    
    
    return x