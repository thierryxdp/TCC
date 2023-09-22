def conta_numero(numero,matriz):
    """Funcao que calcula e retorna quantas vezes aquele numero aparece na matriz;
    int,list->int"""
    cont=0
    for i in range(len(matriz)):
        for j  in range(len(matriz[0])):
            if matriz[i][j]==numero:
                cont=cont+1
    return cont