def conta_numero(numero,matriz):
    """retorna quantas vezes um numero aparece em uma matriz.(list->int)"""
    vezes=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]==numero:
                vezes+=1
    
    return vezes