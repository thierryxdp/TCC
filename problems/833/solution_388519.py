def conta_numero(numero,matriz):
    '''essa funçao conta quantaz vezes um numero dado como entrada aparece na matriz
    int, list -> int'''
    qtd=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]== numero:
                list.count (matriz[i], numero)
                qtd=qtd+1
    return qtd