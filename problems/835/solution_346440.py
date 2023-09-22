def melhor_volta(matriz):
    a=0
    for i in matriz:
        for j in matriz[i]:
            if j == min(matriz[i][0]):
            
            return (i-1, j)