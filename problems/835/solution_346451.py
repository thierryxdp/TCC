def melhor_volta(matriz):
    menor = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            list.append(menor,matriz[i][j])
            if matriz[i][j] == min(menor):
                return (i+1, matriz[i][j], j+1)