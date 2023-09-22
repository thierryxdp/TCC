def soma_h(n):
    """
    Funçâo que recebe um número N e faz a somatória de uma sequência retornando este valor reduzido para duas casas decimais.
    int -> float
    """
    acumulador = 0
    for i in range(1, n + 1):
        H = 1 / i
        acumulador += H

    return round(acumulador, 2)