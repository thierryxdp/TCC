def melhor_volta(matriz):
    menor = []
    for i in range(6):
        for j in range(10):
            list.append(menor,matriz[i][j])
            if matriz[i][j] == min(menor):
                return (i+1, matriz[i][j], j+1)