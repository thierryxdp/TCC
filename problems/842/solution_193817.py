#Recebe uma lista contendo duas listas
#Retorna um dicionário com o número do time e o número de pontos

def pontos_por_time(x):
    time1 = x[0][0]
    time2 = x[0][1]
    golcorcasa1 = x[0][2][0]
    golflafora1 = x[0][2][1]
    golflacasa2 = x[1][2][0]
    golcorfora2 = x[1][2][1]
    
    pontoscor1 = pontoscor2 = pontoscor3 = pontoscor4 = pontoscor5 = pontoscor6 = 0
    pontosfla1 = pontofla2 = pontosfla3 = pontosfla4 = pontosfla5 = pontosfla6 = 0
    
    if golcorcasa1 > golflafora1:
    	pontoscor1 += 3
    	pontosfla1 += 0
        
    if golflafora1>golcorcasa1:
    	pontoscor2 =0
    	pontosfla2 =3
    
    if golflacasa2>golcorfora2:
    	pontoscor3 =0 
    	pontosfla3 =3
       
    if golcorfora2>golflacasa2:
    	pontoscor4 = 3
    	pontosfla4 = 0
        
    if golcorcasa1 == golflafora1:
    	pontoscor5 =1 
        pontosfla5 =1 
        
    else:
        pontoscor5 = pontoscor5
        pontosfla5 = pontosfla5
        
    if golcorfora2 == golflacasa2:
    	pontoscor6 =1
        pontosfla6 =1
        
    totalcor = pontoscor1+pontoscor2+pontoscor3+pontoscor4+pontoscor5+pontoscor6
    totalfla = pontosfla1+pontosfla2+pontosfla3+pontosfla4+pontosfla5+pontosfla6
    
    return {x[0][0] : totalcor, x[0][1] : totalfla}