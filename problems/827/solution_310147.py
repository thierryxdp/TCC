def qtd_divisores(n):
    conta = 0
    for i in range(1, int(n / 2)):
        if n % i == 0:
            conta += 1

    return conta