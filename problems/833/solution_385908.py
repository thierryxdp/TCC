def conta_numero(numero,matriz):
    """ Função que conta quantas vezes um número inteiro aparece em uma dada matriz
    int,list -> int """
    qtd=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]==numero:
                qtd=qtd+1
    return qtd