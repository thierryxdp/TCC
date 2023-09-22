def conta_numero(numero,matriz):
    '''
    funcao criada para retornar quantas vezes um numero aparece na matriz
    parametros:
    numero: numero a ser quantificado
    matriz: matriz de qualquer tamanho
    saida:
    quantidade de vezes que o numero aparece na matriz
    '''
    contador = 0
    
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[i])):
            if matriz[i][j] == numero:
                contador = contador+1
    
    return contador