def melhor_volta(matriz):
    matriz = []
    linhas = len(matriz)
    colunas = len(matriz[0])
    minimo = matriz[0][0]
    tupla = (1,matriz[0][0],1)
    for i in range(linhas):
        for j in range(colunas):
            if matriz[i][j]<minimo:
            minimo = matriz[i][j]
            tupla = (i+1,minimo,j+1)
    print (minimo)