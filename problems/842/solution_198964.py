def pontos_por_time(x):
    ''''''
    
    resultado = dict()
    
    time1 = x[0][0]
    time2 = x[0][1]
    
    pontos1 = int()
    pontos2 = int()
    
    if x[0][2][0] > x[0][2][1]:
    	pontos1 += 3
    
    if x[0][2][0] < x[0][2][1]:
    	pontos2 += 3
        
    if x[0][2][0] == x[0][2][1]:
    	pontos1 += 1
        pontos2 += 1
        
    if x[1][2][0] > x[1][2][1]:
    	pontos2 += 3
    
    if x[1][2][0] < x[1][2][1]:
    	pontos1 += 3
        
    if x[1][2][0] == x[1][2][1]:
    	pontos1 += 1
        pontos2 += 1
        
    resultado = {time2:pontos2, time1:pontos1}
    return resultado