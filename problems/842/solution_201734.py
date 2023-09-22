def pontos_por_time(x):
    
    c = x[0][2][0]
    d = x[0][2][1]
    e = x[1][2][0]
    f = x[1][2][1]
    
    
    time1 = x[0]
    time2 = x[1]
    
    if c > d and e > f:
         return {time1 : 3, time2 : 3}
        
    elif c < d and e > f:
         return {time1 : 0, time2 : 6}
        
    elif c > d and e < f:
         return {time1 : 6, time2 : 0}
        
    elif c < d and e < f:
         return {time1 : 3, time2 : 3}
        
    elif c == d and e == f:
        
         return {time1 : 2, time2 : 2}
        
    elif c == d and e > f:
         return {time1: 1, time2: 4}
    
    elif c > d and e == f:
        return {time1: 4, time2: 1}
    
    elif c == d and e < f:
        return {time1: 4, time2: 1}
    
    else:
        return {time1: 1, time2: 4}