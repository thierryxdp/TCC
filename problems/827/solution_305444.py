def qtd_divisores(n):
    divisores = list()
    for i in range(1, int(n/2+1)):
        if n % 1 ==0:
            divisores.append(i)
    return divisores