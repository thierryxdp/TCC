def qtd_divisores(n):
    """função que recebe um número inteiro n e retorna a
    quantidade de divisores que esse número tem.
    int -> int"""
    intervalo = range(1,n+1)
    divisores = []

    for numero in intervalo:
        if n % numero == 0:
            divisores += [numero]

    return len(divisores)