def melhor_volta(matriz):
    nlin = len(matriz)
    ncol = len(matriz[0])
    C =[]
    for i in range(nlin):
        for j in range(ncol):
            C.append(matriz[i][j])
            menor = min(C)
            if menor in C[0:10]:
                x = 1
                y = C.index(menor)+1
            elif menor in C[10:20]:
                x = 2
                y =C.index(menor)-9
            elif menor in C[20:30]:
                x = 3
                y = C.index(menor)-21
            elif menor in C[30:40]:
                x = 4
            elif menor in C[40:50]:
                x = 5
            elif menor in C[50:60]:
                x = 6
            
                
            
            
                
            
           
    return (x,menor,y)