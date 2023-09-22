def conta_numero(numero,matriz):
    """ função que dado um numero inteiro e uma matriz de inteiros, conta e retorna quantas vezes aquele número aparece;
    int, list -> int"""
    contador = 0
    for i in range(len(matriz)):
        for c in range(len(matriz[0])):
            if matriz[i][c] == numero:
                contador = contador + 1
    return contador