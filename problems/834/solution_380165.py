def media_matriz(m):
    
    acumulas = 0
    divides = (acumulas// (len(m[i]) * len(m))) 
    
    i = 0
    
    for i in range(len(m)):
        
        for j in range(len(m[i])):
                acumulas = acumulas + m[i][j]
    
    return len(m[i])