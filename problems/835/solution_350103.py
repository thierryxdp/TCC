def melhor_volta(matriz6x10):
    menor_tempo = (0, matriz6x10[0][0],0)
    for i in range(6):
        for j in range(10):
            if matriz6x10[i][j] < matriz6x10[volta_corredor[0]][volta_corredor[1]]:
                menor_tempo =  (i+1,matriz6x10[i][j],j+1)
    return (menor_tempo)