def fatorial(n):
    """
    Essa função retorna o fatorial de um determinado número.
	Parametro de entrada: int
    Valor de retorno: int
    """
    i = 0
    fatorial = 1
    n2 = n
    while i < n:
        fatorial = fatorial * n2
        n2 = n2 - 1
        i = i + 1
    return fat