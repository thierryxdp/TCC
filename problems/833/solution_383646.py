def conta_numero(numero,matriz):
    """funcao que calcula a quantidade de vezes que um numero aparece em uma matriz;
    int,list->int"""
    qtd=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]==numero:
                qtd=qtd+1
    return qtd