def qtd_divisores(n):
    num_divisores = 0
    for i in range(1, n, -1):
        if n % i == 0:
            num_divisores+= i
    return num_divisores