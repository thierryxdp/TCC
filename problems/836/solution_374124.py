def busca(string,matriz):
    
    vazia=[]
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] in string:
                matriz.remove(matriz[i][j])
                vazia.append(matriz[i])
                
    return vazia