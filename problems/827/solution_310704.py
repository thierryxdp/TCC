def qtd_divisores(num):
    qtd = 0
    i = 1
    while i <= num:
        if num % i == 0:
            qtd += 1
        i = i + 1
    return qtd