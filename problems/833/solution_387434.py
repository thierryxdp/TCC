def conta_numero(n, m):
    """
    Código que retorna quantas vezes índice n apareceu na matriz
    :n --> int:
    :m --> list:
    :return --> int:
    """
    acumulas = 0
    i = 0
    for i in range(len(m)):
        
        for j in range(len(m[i])):
            if n == m[i][j]:
                acumulas = acumulas + 1
    return acumulas