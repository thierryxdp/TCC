def conta_numero(numero, matriz):
    ''' Função que determina quntas vezes um dado número aparece num matriz
    int -> list '''
    quantidade = 0
    for i in list(range(len(matriz))):
        for j in list(range(len(matriz[0]))):
            if matriz[i][j] == numero:
                quantidade = quantidade + 1
    return quantidade