def qtd_divisores(n:int)->int:
    divisores = 0
    for i in range(1,n+1):
        divisor = i
        if divisor%n==0:
            divisores += 1
    return divisores