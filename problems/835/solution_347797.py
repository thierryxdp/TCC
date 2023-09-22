def melhor_volta(matriz):
    volta_rap=[]
    for i in (matriz):
        indice=list.index(i,min(i))
        list.extend(volta_rap,[min(i),indice])    
	vol=min(volta_rap[0],volta_rap[2],volta_rap[4],volta_rap[6],volta_rap[8],volta_rap[0])
    return (vol,volta_rap)