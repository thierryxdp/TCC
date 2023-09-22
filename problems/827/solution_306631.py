def qtd_divisores(num):
    for x in range(1, num + 1):
        if num % x == 0:
            return x
    while True:
        return 0