def qtd_divisores(n):
    asf = 0
    for i in range(n,0):
        if i % n == 0:
            asf += 1
            print(asf)