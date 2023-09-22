def busca(string,matriz):
    resposta=0
    
    for x in range(len(matriz)):
        for y in range(len(matriz[x])):
            if string == matriz[x][y]:
                resposta=resposta,matriz[x]
    
    
    return resposta