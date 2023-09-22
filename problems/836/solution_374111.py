def busca(string,matriz):
    
    vazia=[]
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] in string:
                vazia.append(matriz[i][0])
                vazia.append(matriz[i][1])
                vazia.append(matriz[i][2])
                
    return vazia