def qtd_divisores(n):
    divisores=0
    for divisor in range(1,n+1):
        if n%divisor==0:
            divisores+=1
    return divisores