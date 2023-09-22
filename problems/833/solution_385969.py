def conta_numero(n,m):
    """ Dado um número n e uma matriz m calcula quantas vezes o número n aparece
    int,list -> int"""
    a = 0
    for e in range(len(m)):
        for f in range(len(m[0])):
            if n == m[0][f]:
                a = a + 1
    return a