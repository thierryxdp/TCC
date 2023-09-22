def conta_numero(numero,matriz):
    """Funcao que, dado um numero inteiro e uma matriz de inteiros, conta e retorna quantas vezes aquele numero aparece na matriz
    int, list -> int"""
    vezes=0
    for a in range(len(matriz)):
        for b in range(len(matriz[0])):
            if numero==matriz[a][b]:
                vezes=vezes+1
            else:
                vezes=vezes
    return vezes