def pontos_por_time(x):
    time1 = x[0][0]
    time2 = x[0][1]
    golcorcasa1 = x[0][1][0]
    golflafora1 = x[0][1][1]
    golflacasa2 = x[1][1][0]
    golcorfora2 = x[1][1][1]
    
    pontoscor = 0
    pontosfla = 0
    
    if golcorcasa1 > golflafora1:
    	pontoscor = pontoscor + 3
    	pontosfla = pontosfla + 0
    
    else:
        pontoscor = pontoscor
        pontosfla = pontosfla
        
    if golflafora1>golcorcasa1:
    	pontoscor = pontoscor + 0
    	pontosfla = pontosfla + 3
    else:
        pontoscor = pontoscor
        pontosfla = pontosfla
    
    if golflacasa2>golcorfora2:
    	pontoscor = pontoscor + 0
    	pontosfla = pontosfla + 3
        
    else: 
        pontoscor = pontoscor
        pontosfla = pontosfla
        
    
    if golcorfora2>golflacasa2:
    	pontoscor = pontoscor + 3
    	pontosfla = pontosfla + 0
        
    else:
        pontoscor = pontoscor
        pontosfla = pontosfla
        
    if golcorcasa1 == golflafora1:
    	pontoscor = pontoscor + 1
        pontosfla = pontosfla + 1
        
    else:
        pontoscor = pontoscor
        pontosfla = pontosfla
        
    if golcorfora2 == golflacasa2:
    	pontoscor = pontoscor + 1
        pontosfla = pontosfla + 1
        
    else:
        pontocor = pontoscor
        pontosfla = pontosfla
        
    totalcor = pontoscor
    totalfla = pontosfla
    
    return {x[0][0] : totalcor, x[0][1] : totalfla}