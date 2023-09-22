def conta_numero(numero,matriz):
    """Essa função conta a quantidade que um número dado aparece na matriz.
    Como entrada temos o número e uma matriz, e como saída temos a contagem;
    int,list->int"""
    contagem=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]== numero:
                contagem+=1