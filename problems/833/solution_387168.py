def conta_numero(numero, matriz):

    '''
    Função que recebe um número e uma matriz como parâmetro
    e retorna quantas vezes esse número aparece na matriz.

    int, matriz -> int
    '''
    
    lin = len(matriz)
    col = len(matriz[0])
    cont = 0

    if matriz == []:
        return 0

    for i in range(lin):
        for j in range(col):
            if matriz[i][j] == numero:
                cont += 1
            
    return cont