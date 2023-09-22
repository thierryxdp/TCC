def qtd_divisores(numero):

    """Retorna a quantidade de divisores um número tem;

    int -> int"""

    i = 1

    soma = 0

    while  i <= numero:

        if numero % i == 0:

            soma += 1

        i = i+1

    return soma