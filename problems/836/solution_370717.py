def busca(string,matriz):
    resposta=[]
    
    for x in len(matriz):
        for y in len(matriz[x]):
            if string == matriz[x][y]:
                resposta+=matriz[x]
    
    
    
    return resposta