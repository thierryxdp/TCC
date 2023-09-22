def fatorial(numero):
    """Função que dado um número, retorna o fatorial deste número; int -> int"""

    n_fatoriais = range(1,numero)
    indice = 0

    while indice < numero:
        numero = numero * n_fatoriais[indice]

        indice += 1

    return numero