def conta_numero(num,matriz):
    contando=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]==num:
                contando+=1
    return contando