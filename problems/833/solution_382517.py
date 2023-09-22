def conta_numero(numero,matriz):
    """conta e retorna quantas vezes o numero aparece na matriz
    int,list(list)->int"""
    a=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if numero==matriz[i][j]:
                list.append(a,numero)
    return len(a)