def qtd_divisores(n):
    """ Essa função conta quantos divisores um número tem.
    int->int."""
    soma = 0
    for i in range(1, n):
        if n % i == 0: 
            soma = soma +1
    return soma