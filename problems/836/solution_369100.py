def busca(nome,matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if nome in matriz[i][j]:
                list.remove(matriz,matriz[i][j])
                return 'ola'