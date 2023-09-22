def conta_numero(numero,matriz):
    """conta a quantidade de vezes um numero aparece dentro de uma matriz"""
    quantidade=0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if martiz[i][j]==numero:
                quantidade=quantidade+1
        return quantidade