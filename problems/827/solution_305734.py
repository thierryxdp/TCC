def qtd_divisores(n:int)->int:
    divisores = []
    for i in range(1,n+1):
        divisor = i
        if divisor%n==0:
            divisores += [divisor]
    return divisores