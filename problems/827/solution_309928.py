def qtd_divisores(x):
    a = 0
    for n in range(1, x):
        if x%n == 0:
            a += 1
        else:
            a += 0
    return a