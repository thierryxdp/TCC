def conta_frases(x):
    
    
    
    interrog=x.count('?')
    exc=x.count('!')
    ponto=x.count('.')
  
    
        
    x=retcs+interrog+exc+ponto
    
    if x.count('...')>0:
        rects=x.count('...')-3
    else: 
        retcs=0
    
    return x