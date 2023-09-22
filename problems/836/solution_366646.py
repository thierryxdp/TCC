def busca(string,matriz):
    retorna=[]
    for i in range(len(matriz)):
        if string==matriz[i][2]:
            matriz[i].remove(string)
            retorna.append(matriz[i])
    return retorna,matriz