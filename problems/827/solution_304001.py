def qtd_divisores(numero:int) -> int:
    """Função que irá contar quntos divisores um número tem.
    int -> int

    Parameters:
    numero: número inteiro que será analisado

    Returns:
    número de divisores que o número dado como entrada possui
    """

    soma = 0
    for possivel_divisor in range(1, numero):
        if possivel_divisor%0 == 0:
            soma = soma + 1
    return soma