def melhor_volta(matriz):
    corredor1=[]
    corredor2=[]
    corredor3=[]
    corredor4=[]
    corredor5=[]
    corredor6=[]
    for i in range(len(matriz)):
        if i == 0:
        	for j in range(len(matriz[i])):
                list.append(corredor1,matriz[i][j])
        elif i == 1:
            for j in range(len(matriz[i])):
                list.append(corredor2,matriz[i][j])
        elif i == 2:
            for j in range(len(matriz[i])):
                list.append(corredor3,matriz[i][j])
        elif i == 3:
            for j in range(len(matriz[i])):
                list.append(corredor4,matriz[i][j])
        elif i == 4:
            for j in range(len(matriz[i])):
                list.append(corredor5,matriz[i][j])
        elif i == 5:
            for j in range(len(matriz[i])):
                list.append(corredor6,matriz[i][j])
   
    	listatempo=[sum(corredor1),sum(corredor2),sum(corredor3),sum(corredor4),sum(corredor5),sum(corredor6)]
    	resultado= (list.index(listatempo,min(listatempo))+1)
    
               
                
                
                
                
            
                
            
    return resultado