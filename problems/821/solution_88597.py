def fatorial(numero):
    """Função que dado um número, retorna o fatorial deste número; int -> int"""

    n_fatoriais = 1
    i = 1

    while i <= numero:
        n_fatoriais = n_fatoriais * i
        i += 1

    return n_fatoriais