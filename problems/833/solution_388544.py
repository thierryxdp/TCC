def conta_numero(numero, matriz):
    '''verifica na matriz um numero e se existe conta e retorna quantas vezes
    :param numero: int->int
    :param matriz: list->list
    :return: int->int
    '''
    contador = 0
    for lin in range(0, len(matriz)):
        for col in range(0, len(matriz[lin])):
            if matriz[lin][col] == numero:
                contador +=1
                
    return contador