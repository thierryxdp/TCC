def busca(string,matriz):
    retorna=[]
    for i in range(len(matriz)):
        if string==matriz[i][2]:
            retorna.append(matriz[i].remove(string))
    return matriz[0][1]