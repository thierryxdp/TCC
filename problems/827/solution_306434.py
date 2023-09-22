def qtd_divisores(n):
    divisores=0
    for x in range(n):
        if x != 0 and n > 0:
            if n%x == 0:
                divisores=divisores+1
    return divisores +1
    for x in range(n):
        if x != 0 and n < 0:
            if n%x == 0:
                divisores=divisores+1
    return divisores