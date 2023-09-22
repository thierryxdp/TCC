def busca(string,matriz):
    cont=[]
    for i in range(len(matriz)):
        for string in matriz[i][2]:
            del(matriz[i][2])
            cont+=[matriz[i]]
    return cont