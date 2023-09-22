def qtd_divisores(n):
    """função que calcula a quantidade de divisores que um numero tem;
    int->int"""
    divisor = 0 
    for i in range (n+1):
        if i != 0 and n%i == 0:
            divisor += 1
    return divisor