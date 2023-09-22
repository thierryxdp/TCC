def conta_numero(numero,matriz):
    '''
    Conta quantas vzs um numero aparece na matriz
        Parametros:
            numero,matriz: int,list
        Saida: int
    '''
    lista = []

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
                lista += [matriz[i][j]]

    return len(lista)