def qtd_divisores(numero):

    """Dado um número, conta quantos divisores esse número tem

    int -> int"""

    contador = 0

    for x in range(numero):

        if numero%(x+1) == 0:

            contador = contador + 1

    return contador