def faltante(x):
    y = [0] + x + [0]
    a = 0
    b = list(range(len(x)+2)) + [x] + [0]
    while a <= len(x):
        if b[a] != y[a]:
            return y[a-1] + 1
        a += 1