def busca(string,matriz):
    
    vazia=[]
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] in string:
                vazia.append(matriz[i])
    
    for l in range(len(vazia)):
        for k in range(len(vazia[l])):
            if vazia[l][k] in string:
                del vazia[i]

                
    return len(vazia)