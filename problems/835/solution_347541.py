def melhor_volta(matriz):
    melhortempo = 99999999
    corredor = 0
    volta = 0
    for i in range(6):
        for j in range(10):
            if matriz[i][j] < melhortempo:
                melhortempo = matriz[i][j]
                corredor = i+1
                volta = j+1
    return (corredor,melhortempo,volta)