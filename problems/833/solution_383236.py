def conta_numero(n, m):
    '''Conta quantas vezes um dado número aparece em uma matriz
int, list -> int'''
    vezes = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == n:
                vezes += 1
    return vezes