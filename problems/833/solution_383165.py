def conta_numero(numero,matriz):

    """ A função visita todos os valores das matrizes, ou listas de lista
        e conta quantas vezes o número fornecido na função aparece na matriz.
        int,list -> int
    """

    contador = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):

            if matriz[i][j] == numero:
                contador = contador + 1
                
    return contador