def busca(string,matriz):
    
    for x in range(len(matriz)):
        for y in range(len(matriz[x])):
            resposta=[]
            if string == matriz[x][y]:
                resposta+=matriz[x]
    
    
    return resposta