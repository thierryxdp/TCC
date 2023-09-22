def qtd_divisores(n):
    asf = 1
    for i in range(n,-1,-1):
        if i % n == 0:
            asf += 1
            print(asf)