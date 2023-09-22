def melhor_volta(matriz):
    for i in range(6):
        cont = 0
        for j in range(10):
            if matriz[i][j] == min(max(matriz)):
                tupla = (i+1,matriz[i][j],j+1)
                cont = cont + 1
    return tupla