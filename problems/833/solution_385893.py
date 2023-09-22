def conta_numero(n, m):
    '''Função que calcula e  retorna quantas vezes aquele número(n) aparece na matrriz. int,list(list)->int'''
    c = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == n:
                c = c + 1
    return c