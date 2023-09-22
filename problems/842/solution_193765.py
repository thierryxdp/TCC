#Recebe uma lista contendo duas listas
#Retorna um dicionário com o número do time e o número de pontos

def pontos_por_time(x):
    time1 = x[0][0]
    time2 = x[0][1]
    golcorcasa1 = x[0][2]
    golflafora1 = x[0][3]
    golflacasa2 = x[1][2]
    golcorfora2 = x[1][3]
    
    pontoscor = 0
    pontosfla = 0
    
    if golcorcasa1 > golflafora1:
    	pontoscor = pontoscor + 3
    	pontosfla = pontosfla + 0
    
    elif golflafora1>golcorcasa1:
    	pontoscor = pontoscor + 0
    	pontosfla = pontosfla + 3
    
    elif golflacasa2>golcorfora2:
    	pontoscor = pontoscor + 0
    	pontosfla = pontosfla + 3
    
    elif golcorfora2>golflacasa2:
    	pontoscor = pontoscor + 3
    	pontosfla = pontosfla + 0
    
    totalcor = pontoscor
    totalfla = pontosfla
    
    return {x[0][0] : totalcor, x[0][1] : totalfla}