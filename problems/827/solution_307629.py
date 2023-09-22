def qtd_divisores(num):
    i = 2
    q = 1
    while i < num:
        if num % i == 0:
            q += 1
    return q