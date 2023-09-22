def melhor_volta(matriz):
    ''''''
    variavel = (0, float('inf'), 0)

    for i in range(6):
        for j in range(10):
            if matriz[i][j] < variavel[1]:
                variavel = (i+1, matriz[i][j], j+1)
   
    return variavel