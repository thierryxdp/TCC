def conta_numero(numero, matriz):
    """dado um número inteiro e uma
matriz de inteiros de tamanho qualquer,
conta e retorna quantas vezes aquele
número aparece na matriz"""
    nlin = len(matriz) #qnt de linha
    ocorrencia = 0 #quantas vezes o numero aparece na matriz
    
    if nlin == 0:
        return 0
    
    for i in range(nlin): 
        ncol = len(matriz[0]) #qnt de coluna
        for j in range(ncol):
            if matriz[i][j] == numero: #verifica as posições na matriz
                ocorrencia += 1

    return ocorrencia