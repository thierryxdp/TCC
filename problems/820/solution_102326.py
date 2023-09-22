def posLetra (x,y,z):
    
    
    
    i = 0
    v = 0
    
    while len(x)>i:
        if x[i] ==  y:
            v = v + 1
        if x[i] == y and v == z:
            return i
        
    return -1