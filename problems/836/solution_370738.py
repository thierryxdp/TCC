def busca(string,matriz):
    resposta=[]
    
    for x in range(len(matriz)):
        for y in range(len(matriz[x])):
            if string == matriz[x][2]:
                i= matriz[x]
                j=i.remove(i[2])
                resposta.append(matriz[x])
    
    
    return resposta