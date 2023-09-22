def conta_numero(n,m):
    '''returna quantas vezes o numero (n) aparece na matriz de inteiros (m)
    int, matriz -> int'''
    resul = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == n:
                resul = resul + 1
    return resul