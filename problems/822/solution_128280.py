def repetidos(x):
    r = 0
    ft = x[1:]
    ls = x
    for c in range(len(ft)):
        if ft[c]==ls[c]:
            return r + 1
        else:
            return r