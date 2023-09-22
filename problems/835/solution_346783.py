def melhor_volta(m):
    linhas = len(m)
    colunas = len(m[0])
    minimo = matriz[0][0]
    tupla = (1,matriz[0][0],1)
    for i in range(linhas):
        for j in range(colunas):
        if matriz[i][j]<minimo:
            minimo = matriz[i][j]
            tupla = (i+1,minimo1j+1)
    print (minimo)