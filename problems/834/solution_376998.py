def media_matriz(matriz):
    variavelSoma=0
    variavelElementos=0
    for i in range(len(matriz)):
        for elementosMatriz in range(len(matriz[0])):
            variavelSoma+=matriz[i][elementosMatriz]
            variavelElementos+=1
    TudoSomado=variavelSoma/variavelElementos
    return round(TudoSomado,2)