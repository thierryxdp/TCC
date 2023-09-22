def melhor_volta(matriz):
    corredor1=[]
    corredor2=[]
    corredor3=[]
    corredor4=[]
    corredor5=[]
    corredor6=[]
    listatotal=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            list.append(listatotal,matriz[i][j])
            
        
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[0][j] in min(listatotal):
                
            elif matriz[1][j] in min(listatotal):
                return (2,min(listatotal),j)
            elif matriz[2][j] in min(listatotal):
                return (3,min(listatotal),j)
            elif matriz[3][j] in min(listatotal):
                return (4,min(listatotal),j)
            elif matriz[4][j] in min(listatotal):
                return (5,min(listatotal),j)
            elif matriz[5][j] in min(listatotal):
                return (6,min(listatotal),j)