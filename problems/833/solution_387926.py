def conta_numero(n, matriz):
    
    i = 0
    
    for x in matriz:
        for y in x:
            if y == n:
                i += 1
    return i