def qtd_divisores(y):
    sum = 1

    for i in range(y):
        if (i == 0):
            continue
            sum = sum+(1/i)
    return sum