def qtd_divisores(n):
    asf = 0
    for i in range(n,-1,-1):
        i % n
        if i % n == 0:
            asf += 1
            print(asf)