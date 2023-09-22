def busca(string,matriz):
    for i in range(len(matriz)):
        matrizz=[]
        for j in range(len(matriz[i])):
            if string == matriz[i][j]:
                matrizz=matriz[i]
                return matrizz