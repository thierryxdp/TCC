def soma_h(n):
    """A função retorna o valor de H.
    int -> int """
        soma = 0
    for c in range(1, n + 1):
        inverso = (1/c)
        soma += inverso
    return round(soma, 2)