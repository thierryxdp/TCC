def qtd_divisores(x):
    r = 0
    for a in list(range(x+1))[1::]:
        if x%a == 0:
            r += 1
    return r