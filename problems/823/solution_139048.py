def faltante(x):
    
    i = 0
    
    while x[i] < x[i + 1]:
        i += 1
        
    return x[i + 1] - 1