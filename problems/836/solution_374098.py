def busca(string,matriz):
    
    vazia=[]
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] in string:
                vazia.append(matriz[i])
                if vazia==matriz[i][j]:
                    vazia.remove(matriz[i])
                
    return vazia