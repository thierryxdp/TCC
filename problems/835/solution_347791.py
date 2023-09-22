def melhor_volta(matriz):
    volta_rap=[]
    for i in (matriz):
        indice=list.index(i,min(i))
        list.extend(volta_rap,[min(i),indice])    
	vol=min(volta_rap)
    return volta_rap