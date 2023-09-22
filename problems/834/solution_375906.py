def media_matriz(a):
    """ Retorna a média de todos os números da matriz a; list -> float """
    elementos=len(a)*len(a[0]);
    c=0
    for i in range(len(a)):
        for j in range(len(a[0])):
            c=c+a[i][j]
    return c/elementos