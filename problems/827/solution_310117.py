def qtd_divisores(n):
    a = 0
    for x in range(n):
        if n%x == 0:
            a += 1
    return a