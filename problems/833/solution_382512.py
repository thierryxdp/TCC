def conta_numero(numero,matriz):
    """conta e retorna quantas vezes o numero aparece na matriz
    int,list(list)->int"""
    a=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if numero in matriz[i][j]:
                list.append(numero,a)
    return len(a)