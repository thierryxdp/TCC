def qtd_divisores(n:int)->int:
    divisores = 0
    for i in range(n):
        if (i%n == 0):
            divisores += 1
    return divisores