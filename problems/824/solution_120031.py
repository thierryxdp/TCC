def uppCons(x):
    
    z = ''
    i = 0
    
    while i < len(x):
        if x[i] not in 'a' or x[i] not in 'e' or x[i] not in 'i' or x[i] not in 'o' or x[i] not in 'u':
            
         z += str.upper(x[i])    
         i += 1
    return z