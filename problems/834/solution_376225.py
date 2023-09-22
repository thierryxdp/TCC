def media_matriz(matriz):
    '''funcao que retorna a media de todos os numeros da matriz
    list->float''''
    somatorio=0
    linha=0
    coluna=0
    for i in range(len(matriz)):
        linha=linha+1
        for j in range(len(matriz[0])):
            somatorio=somatorio+matriz[i][j]
            coluna=j+1
    x=linha*coluna
    resultado=somatorio/x
    return round(resultado,2)