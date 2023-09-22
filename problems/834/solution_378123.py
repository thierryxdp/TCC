def media_matriz(matriz):
    '''
    funcao criada para retornar a media dos numeros de uma matriz 
    parametros:
    matriz: matriz de numeros inteiros 
    saida:
    media dos numeros da matriz 
    '''
    soma = 0
    tamanho = 0
    media = 0 
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            tamanho = tamanho+1
            soma = soma+matriz[i][j]
            media = soma/tamanho