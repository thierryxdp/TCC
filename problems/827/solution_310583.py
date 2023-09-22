def qtd_divisores(x):
    divisores = 0
    for divisor in range(1,x+1):
        if x%divisor == 0:
            divisores = divisores + 1
    return(divisores)