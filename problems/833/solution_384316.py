def conta_numero(n,m):
    '''função que retorna quantas vezes o número n aparece na matriz m
    int, list -> int'''
    numero = 0
    for i in len(m):
        for j in len(m[i]):
            if m[i][j] == n:
                numero += 1
    return numero