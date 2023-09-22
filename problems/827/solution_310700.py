def qtd_divisores(num):
    qtd = 0
    for i in range(1, num + 1):
        if num % i == 0:
            qtd += 1
    return qtd