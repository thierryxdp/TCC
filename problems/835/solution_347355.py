def melhor_volta(matriz):
    aux = ()
    for i in range(0,6):
        for j in range(0,10):
            aux += matriz[i][j],
    for i in range(0,6):
        for j in range(0,10):
            if matriz[i][j] == min(aux):
                corredor = i+1
                volta = j+1
    return (corredor, min(aux), volta)