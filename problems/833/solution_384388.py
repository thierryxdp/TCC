def conta_numero(n,m):
    """Função que recebe um numero e uma matriz e retorna quantas
    vezes aquele numero aparece na matriz
    int, lista --> int"""
    r = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == n:
                r = r + 1
	return r