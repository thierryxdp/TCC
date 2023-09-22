def media_matriz(matriz):
    num=0
    n=0
    for i in range(matriz):
        num=num+sum(i)
        n=n+len(i)
    return round(num/n,2)