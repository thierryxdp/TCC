def conta_numero(numero, matriz):
    """ Função que dado um inteiro e uma matriz, 
    conta ae retorna quantas vezes aquele número aparece na matriz
    list, int -> int"""
    contador = 0
    for lin in range(0, len(matriz)):
        for col in range(0, len(matriz[lin])):
            if matriz[lin][col] == numero:
                contador += 1

    return contador