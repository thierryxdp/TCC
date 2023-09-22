def melhor_volta(matriz):
    cont = 0
    for i in range(6):
        cont = 0
        for j in range(10):
            if matriz[i][j] == min(matriz[i]):
                tupla = (i+1,matriz[i][j],j)
                cont = cont + 1
     return tupla