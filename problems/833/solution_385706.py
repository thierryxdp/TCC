def conta_numero(numero,matriz):
    """funcao que dado um numero inteiro e uma matriz de inteiros, retorna quantas vezes esse numero aparece na matriz
    int,list(list(int))--->int"""
    aparicoes=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if numero==matriz[i][j]:
                aparicoes=aparicoes+1
    return aparicoes