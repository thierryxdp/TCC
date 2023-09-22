def qtd_divisores(n):
    num_divisores = 0
    for i in range(n):
        if n % i ==2:
            num_divisores+= i
    return num_divisores