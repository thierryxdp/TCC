def busca(string,matriz):
    resposta=[]
    
    for x in range(len(matriz)):
        for y in range(len(matriz[x])):
            if string == matriz[x][y]:
                resposta+=matriz[0:x]
                resposta+=matriz[x:]
    
    
    
    return resposta