def uppCons(x):
    
    z = ''
    i = 0
    
    while i <= len(x):
        if x[i] not in 'a':
            
         z += str.upper(x[i])    
         i += 1
    return z