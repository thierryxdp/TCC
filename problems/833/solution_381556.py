def conta_numero(numero,matriz):
    '''função que dado um número inteiro e uma matriz de inteiros de tamanho qualquer, conta e retorna quantas vezes aquele número aparece na matriz.
    Entrada: int, list;
    Saída: int'''
    contador = 0
    for i in range(len(matriz)):
        for c in range(len(matriz[0])):
            if matriz[i][c] == numero:
                contador = contador + 1
    return contador