def busca(string,matriz):
    resposta=[]
    
    for x in range(len(matriz)):
        for y in range(len(matriz[x])):
            if string == matriz[x][y]:
                resposta=resposta+matriz[x][0,3:-1]
    return resposta