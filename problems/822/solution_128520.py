def repetidos(x):
    
    i = 0
    j = 0
    
    while i < len(x):
        if x[i] == x[i + 1]:
            
            j +=1
            
        i += 1
            
    return j