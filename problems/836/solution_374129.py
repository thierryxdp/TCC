def busca(string,matriz):
    
    vazia=[]
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] in string:
                vazia.append(matriz[i])
                
    for l in range(len(vazia)):
        if string in vazia[i]:
            vazia.remove(vazia[i])
                
                
    return vazia