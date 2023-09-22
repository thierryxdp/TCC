def qtd_divisores(n):
    """ Essa função conta quantos divisores um número tem.
    int->int."""
    soma = 0
    for i in range(0,n+1):
        result = n//i
        if n%i == 0:
            soma = soma +result
            return soma