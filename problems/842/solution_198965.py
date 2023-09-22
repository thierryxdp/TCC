def pontos_por_time(x):
    '''Essa função retorna o saldo de pontos de dois times que jogaram dois jogos, 
    um contra contra o outro,
    list[[string,string[int,int]],[string,string[int,int]]] -> dict{}'''
    
    resultado = dict()
    
    # nomes dos times
    time1 = x[0][0]
    time2 = x[0][1]
    
    #armasenar os pontos
    pontos1 = int()
    pontos2 = int()
    
    # se o time1 vencer ganha 3 pontos
    if x[0][2][0] > x[0][2][1]:
    	pontos1 += 3
    
    # se o time2 vencer ganha 3 pontos
    if x[0][2][0] < x[0][2][1]:
    	pontos2 += 3
    
    # se empatar cada um ganha 1
    if x[0][2][0] == x[0][2][1]:
    	pontos1 += 1
        pontos2 += 1
    
    # se o time2 vencer ganha 3 pontos
    if x[1][2][0] > x[1][2][1]:
    	pontos2 += 3
    
    # se o time1 vencer ganha 3 pontos
    if x[1][2][0] < x[1][2][1]:
    	pontos1 += 3
    
    # se empatar cada um ganha 1
    if x[1][2][0] == x[1][2][1]:
    	pontos1 += 1
        pontos2 += 1
        
    resultado = {time2:pontos2, time1:pontos1}
    
    return resultado