def conta_numero(numero,matriz):
    """Funcao que dado um numero inteiro e uma matriz de inteiros de
    tamanho qualquer, conta e retorna quantas vezes aquele numero
    aparece na matriz: int,list(list) -> int"""

    contador = 0
    nlin = len(matriz)
    ncol = len(matriz[0])

    for i in range(nlin):
        for j in range(ncol):
            if matriz[i][j] == numero:
                contador = contador + 1
    return contador