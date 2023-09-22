def pontos_por_time(x):
    
    x[2][0] = c
    x[2][1] = d
    x[5][0] = e
    x[5][1] = f
    
    g = []
    h = []
    time1 = x[0]
    time2 = x[1]
    
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
        
    return { time1 : g + h, time2 : g + h}