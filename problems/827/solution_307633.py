def qtd_divisores(num):
    q = 2
    i = 0
    if num > 0:
        i += 2
        while i < num:
            if num % i == 0:
                q += 1
            i += 1
    return q