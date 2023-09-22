def eh_quadrada(m):
    m = []
    nlin = len(m)
    ncol = len(m[0])
    total = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            total = total + 1
        if nlin-ncol==0:
            return True