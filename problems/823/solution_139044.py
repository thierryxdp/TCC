def faltante(x):
    
    i = 0
    j = []
    
    while x[i] == x[i + 1] - 1:
        i += 1
        j += [x[i] + 1]
        
    return j