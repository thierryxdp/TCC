def faltante(x):
    y = [0] + x + [0]
    a = 0
    b = [0] + list(range(len(x)+1)[1::]) + [x] + [0]
    while a <= len(x):
        if b[a] != x[a]:
            return x[a] - 1
        a += 1