def melhor_volta(matriz):
    ''' idéia: pegar a matriz 6x10,
supor que o valor minimo esta na posição m[o][o],
caso nao esteja, fazer o contador andar por toda matriz
achando o menor, assim que achar o menor de todos
ela vai substituir no valor minimo.'''
    matriz = []
    linhas = 6
    colunas = 10
    minimo = matriz[0][0]
    tupla = (1,matriz[0][0],1)
    for i in range(linhas):
        for j in range(colunas):
            if matriz[i][j]<minimo:
                minimo = matriz[i][j]
            tupla = (i+1,minimo,j+1)
    print (minimo)