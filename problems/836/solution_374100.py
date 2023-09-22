def busca(string,matriz):
    
    vazia=[]
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] in string:
                vazia.append(matriz[i])
                if string in matriz:
                    vazia.remove(string)
                
    return vazia