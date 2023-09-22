def melhor_volta(matriz):
    for i in range(6):
        cont = 0
        for j in range(10):
            if matriz[i][j] == min(matriz[0]) or min(matriz[1]) or min(matriz[2]) or min(matriz[3]) or min(matriz[4]) or min(matriz[5]) or min(matriz[6]):
                tupla = (i+1,matriz[i][j],j+1)
                cont = cont + 1
    return tupla