def qtd_divisores(n):
    asf = 0
    for i in n:
        if i % n == 0:
            asf += 1