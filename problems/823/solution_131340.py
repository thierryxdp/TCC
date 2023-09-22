def faltante(x):
    a = 0
    b = list(range(len(x)+1)[1::]) + [x]
    while a <= len(x):
        if x[a] != b[a]:
            return x[a] - 1
        a += 1