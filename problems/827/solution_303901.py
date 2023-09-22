def qtd_divisores(n):
    """ Função que conta o número de divisores.
    int, int->int """
    divisor = []
    for i in range(1,n+1):
        if  n% i==0:
            divisor.append((i, int(n / i)))
    return divisor