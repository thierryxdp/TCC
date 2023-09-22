def qtd_divisores(n):
    """ Essa função conta quantos divisores um número tem.
    int->int."""
    for i in range(1, n+1):
        if n % i == 0: 
            return i
    return n