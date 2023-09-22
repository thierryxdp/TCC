def qtd_divisores(n):
    """ Essa função conta quantos divisores um número tem.
    int->int."""
    x =1
    while x <= n:
        y = n % x
        x = x +1
        if y == 0:
            return (x-1)