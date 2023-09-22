def busca(string,matriz):
    for x in range(len(matriz)):
        for y in range(len(matriz[x])):
            if string == matriz[x][y]:
                return matriz[x]