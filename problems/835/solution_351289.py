def melhor_volta(matriz):
    ''''''
    
    tup=()
    for i in range(6):
        for j in range(10):
            if matriz[i][j] < tup(1):
                tup=(i+1,matriz[i][j],j+1)
    return tup