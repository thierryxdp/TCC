def repetidos(x):
    
    i = 0
    j = 0
    
    while i < len(x)-1:
        if x[i] == x[i + 1]:
            
            j +=1
            
        i += 1
            
    return j