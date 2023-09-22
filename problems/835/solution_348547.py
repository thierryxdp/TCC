def melhor_volta(matriz):
    corredor=[]
    volta=[]
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            tempo =  min(matriz[i][j])
            return tempo