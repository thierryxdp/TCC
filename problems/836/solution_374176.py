def busca(string,matriz):
    
    registro=[]
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] not in string:
                matriz[i][j]==0
                registro.append(matriz[i])

                
    return registro