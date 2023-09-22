def pontos_por_time(x):
    
    c = x[0][2][0]
    d = x[0][2][1]
    e = x[1][2][0]
    f = x[1][2][1]
    
    g = ()
    h = ()
    
    time1 = x[0]
    time2 = x[1]
    
    #jogo de ida
    
    if c > d:
         g = g + (3,)
        
    if c == d:
         g = g + (1,)
        
    if c < d:
         g = g + (0,)
        
    #jogo da volta    
        
    if e > f:
         h = h + (3,)
        
    if e == f:
         h = h + (1,)
        
    if e < f:
         h = h + (0,)
        
    return { time1 : g, time2 : g}