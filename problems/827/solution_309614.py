def qtd_divisores(n):
    """
    Função que recebe um número e calcula a quantidade de divisores que ele pode ter.
    int -> int
    """
    divisores = 0
    for i in range(1, n + 1):
        if n % i == 0:
            divisores += 1

    return divisores