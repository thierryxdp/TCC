def qtd_divisores(num):
    total = 0
    for i in range(num):
        if num % i == 0:
            total += 1
    return total