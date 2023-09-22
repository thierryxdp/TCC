def conta_numero(numero,matriz):
    '''conta a quantidade de vezes que o valor de entrada 
    número está presente na matriz de entrada; float -> list
    '''
    counter = 0
    linhas = len(matriz)
    colunas = len(matriz[0])
    for i in range(linhas):
        for  j in range(colunas):
            if matriz[i][j] == numero:
                counter += 1
            return counter