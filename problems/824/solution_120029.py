def uppCons(x):
    
    z = ''
    i = 0
    
    while i < len(x):
        if x[i] not in 'a' not in 'e' not in 'i' not in 'o' not in 'u':
            
         z += str.upper(x[i])    
         i += 1
    return z