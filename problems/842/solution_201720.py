def pontos_por_time(x):
    
    x[2][0] = c
    x[2][1] = d
    x[5][0] = e
    x[5][1] = f
    
    g = []
    h = []
    
    #jogo de ida
    
    if c > d:
        g = g + [3]
        
    if c = d:
        g = g + [1]
        
    if c < d:
        g = g + [0]
        
    #jogo da volta    
        
    if e > f:
        h = h + [3]
        
    if e = f:
        h = h + [1]
        
    if e < f:
        h = h + [0]
        
    return {'x'[0]: g + h, 'x'[1]: g + h}