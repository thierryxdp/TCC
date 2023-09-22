def media_matriz(a):
    c = 0
    for i in a:
        c = c + sum(i)
    return (c/(len(a[0] + 1)))