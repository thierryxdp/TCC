def busca(string,matriz):
    cont=[]
    for i in range(len(matriz)):
        for string in matriz[i][1]:
            del(matriz[i][1])
            cont+=[matriz[0][1][3]]
    return cont