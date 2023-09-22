def media_matriz(a):
    c = 0
    b = (len(a[0]) + 1)*(len(a))
    for i in a:
        c = c + sum(i)
        print(c)
        print(b)
    return c/b