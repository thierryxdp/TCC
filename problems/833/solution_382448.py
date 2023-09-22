def conta_numero(numero:int, matriz:list)->int:
    """Diz quantas vezes um determinado número inteiro aparece na matriz
       
       Parameters:
       numero: número inteiro a ser procurado
       matriz: matriz qualquer
       
       Returns:
       quantidade de vezes o numero aparece na matriz
    """
    contador = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == numero:
                contador += 1
    return contador