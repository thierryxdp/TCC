def media_matriz(matriz):
    variavelSoma=0
    variavelElementos=0
    for i in range(len(matriz)):
        for elementosMatriz in matriz[variavelElementos]:
            variavelSoma+=sum(matriz[variavelElementos])
        variavelElementos+=1
    return variavelSoma/variavelElementos