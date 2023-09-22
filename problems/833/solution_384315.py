def conta_numero(n,m):
    '''função que retorna quantas vezes o número n aparece na matriz m
    int, list -> int'''
    numero = 0
    for i in m:
        for j in m[i]:
            if m[i][j] == n:
                numero += 1
    return numero