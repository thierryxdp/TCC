def conta_numero(numero,matriz):
    """Essa função retorna a incidencia de um numero dentro de uma matriz"""
    """int,list->int"""
    qtd=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if numero == matriz[i][j]:
                qtd=qtd+1
    return qtd