def busca(string,matriz):
    matrizaberta=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matrizaberta=matrizaberta+matriz[i][j]
    return matrizaberta