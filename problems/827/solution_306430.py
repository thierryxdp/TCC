def qtd_divisores(n):
    divisores=0
    for x in range(n):
        if n%x == 0:
            divisores=divisores+1
    return divisores