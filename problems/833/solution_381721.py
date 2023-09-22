def conta_numero(numero,matriz):
    """Funcao que recebe um numero inteiro e uma matriz e retorna quantas vezes aquele numero aparece na matriz"""
    total=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]==numero:
                total=total+1
    return total