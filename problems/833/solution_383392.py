def conta_numero(numero,matriz):
    '''Ao fornecer um numero inteiro e uma matriz, retorne
    quantas vezes esse numero se repete na matriz.

    int, list -> int'''

    contador = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == numero:
                contador += 1
    return contador