def media_matriz(matriz):
    variavelSoma=0
    variavelElementos=0
    variavelContagem=0
    for i in range(len(matriz)):
        for elementosMatriz in range(len(matriz[variavelElementos])):
            variavelSoma+=sum(matriz[variavelElementos])
            variavelContagem+=len(matriz[variavelElementos])
        variavelElementos+=1
    return variavelSoma/variavelElementos