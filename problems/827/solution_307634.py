def qtd_divisores(num):
    q = 0
    i = 1
    if num > 0:
        while i < num:
            if num % i == 0:
                q += 1
            i += 1
    return q