def qtd_divisores(n):
    """ Função que conta quantos divisores um número tem.
    int, int->int """
    divisor = [1]
    for i in range(2,n):
        if (n % i) == 0:
            divisor.append(i)
    return divisor