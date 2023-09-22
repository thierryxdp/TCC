def busca(string,matriz):
    matrizaberta= 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matrizaberta=matrizaberta,matriz[i][j]
    return matrizaberta