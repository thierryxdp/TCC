def qtd_divisores(num):
    total = []
    for i in range(num):
        if num % i == 0:
            total += [i]
    return total