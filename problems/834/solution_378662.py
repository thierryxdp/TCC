def media_matriz(matriz):
    cont = 0
    linhas = len(matriz[0])
    for i in matriz:
        for j in i:
            cont = cont + j
    return (cont/linhas)