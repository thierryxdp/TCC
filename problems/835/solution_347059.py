def melhor_volta(matriz):
    for i in range(6):
        cont = 0
        for j in range(10):
            if matriz[i][j] == min(matriz[0]):
                if matriz[i][j] == min(matriz[1]):
                    if matriz[i][j] == min(matriz[2]):
                       if matriz[i][j] == min(matriz[3]):
                           if matriz[i][j] == min(matriz[4]):
                               if matriz[i][j] == min(matriz[5]):
                                   if matriz[i][j] == min(matriz[6]):
                                       tupla = (i+1,matriz[i][j],j+1)
                                       cont = cont + 1
    return tupla