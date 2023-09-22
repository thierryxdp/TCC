def conta_numero(n,m):
    """ Dado um número n e uma matriz m calcula quantas vezes o número n aparece
    int,list -> int"""
    a = 0
    for e in m:
        for f in e[0]:
            if n == f:
                a = a + 1
    return a