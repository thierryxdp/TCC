def melhor_volta(matriz):

    c=0 
     
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            c+=1
            a = min(matriz[i][j])

    return a