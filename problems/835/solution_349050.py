def melhor_volta(matriz):
    nlin = len(matriz)
    ncol = len(matriz[0])
    C =[]
    for i in range(nlin):
        for j in range(ncol):
            C.append(matriz[i][j])
            menor = min(C)
            if menor in matriz[i][j]:
                x = matriz[i][j]
                
            
           
    return (menor,x)