def qtd_divisores(numero):
    """Função que dado um número inteiro, retorna quantos divisores tem
    este número; int -> int"""

    divisores = 0

    for divisor in range(1,numero + 1):
        if ((numero % divisor) == 0):
            divisores += 1

    return divisores