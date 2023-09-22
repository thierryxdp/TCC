def busca(string,matriz):
    resposta=[]
    
    for x in matriz:
        for y in matriz[x]:
            if string == matriz[x][y]:
                resposta+=matriz[x]
    
    
    
    return resposta