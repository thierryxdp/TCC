def uppCons(x):
    
    x = ' '
    i = 0
    
    while x[i] <= len(x):
        if x in 'aeiou':
            str.upper(x)
        i += 1
        
    return x