def qtd_divisores(x):
    a = []
    for n in range(1, x):
        if x%n == 0:
            a += n
        else:
            a += []
    return a