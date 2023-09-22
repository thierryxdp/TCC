#Recebe uma lista contendo duas listas
#Retorna um dicionário com o número do time e o número de pontos

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
    	pontoscor1 += 3
    	pontosfla1 += 0
    
    else:
        pontoscor1 = pontoscor
        pontosfla1 = pontosfla
        
    if golflafora1>golcorcasa1:
    	pontoscor2 =0
    	pontosfla2 =3
    else:
        pontoscor2 = pontoscor2
        pontosfla2 = pontosfla2
    
    if golflacasa2>golcorfora2:
    	pontoscor3 =0 
    	pontosfla3 =3
        
    else: 
        pontoscor3 = pontoscor
        pontosfla3 = pontosfla
        
    
    if golcorfora2>golflacasa2:
    	pontoscor4 = 3
    	pontosfla4 = 0
        
    else:
        pontoscor4 = pontoscor
        pontosfla4 = pontosfla
        
    if golcorcasa1 == golflafora1:
    	pontoscor5 =1 
        pontosfla5 =1 
        
    else:
        pontocor = pontoscor
        pontosfla = pontosfla
        
    if golcorfora2 == golflacasa2:
    	pontoscor6 =1
        pontosfla6 =1
        
    else:
        pontoscor6 = pontoscor
        pontosfla6 = pontosfla
        
    totalcor = pontoscor1+pontoscor2+pontoscor3+pontoscor4+pontoscor5+pontoscor6
    totalfla = pontosfla1+pontosfla2+pontosfla3+pontosfla4+pontosfla5+pontosfla6
    
    return {x[0][0] : totalcor, x[0][1] : totalfla}