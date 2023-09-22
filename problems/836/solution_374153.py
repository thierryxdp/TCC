def busca(string,matriz):
    
    vazia=[]
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] in string:
                vazia.append(matriz[i])
    
    for l in range(0,6):
        if vazia[l]==string:
            del vazia[i]

                
    return len(vazia)