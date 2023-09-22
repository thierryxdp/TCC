def conta_numero(matriz,numero):
    """Funcao que, dado uma matriz de inteiros de tamanho qualquer
    e um numero inteiro, retorna quantas vezes o numero aparece na matriz;
    list, int -> int """
    acumulador=0
    for linhas in matriz:
        for aij in linhas:
            if aij==numero:
                acumulador+=1
    return acumulador