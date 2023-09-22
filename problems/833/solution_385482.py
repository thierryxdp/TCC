def conta_numero(numero,matriz):
    """Funcao que, dado um numero inteiro e uma matriz de inteiros de tamanho qualquer,
    retorna quantas vezes o numero aparece na matriz;
    list, int -> int """
    acumulador=0
    for linhas in matriz:
        for aij in linhas:
            if aij==numero:
                acumulador+=1
    return acumulador