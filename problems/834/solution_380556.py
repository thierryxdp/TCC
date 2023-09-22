def media_matriz(m):
    '''
    
    '''
    dividendo = 0
    divisor = 0 
    for i in range(len(m)):
    	for j in range(len(m[i])):
            dividendo += m[i][j]
            divisor += 1   
    return dividendo/divisor