def uppCons(x):
    
    z = ''
    i = 0
    
    while i < len(x):
        if x[i] in 'aeiou':
            z += str.upper(x[i])
        else:
            z += str.upper(x[i])
        i += 1
    return z