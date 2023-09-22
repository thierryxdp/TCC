def fatorial(n):
    """
    Essa função retorna o fatorial de um determinado número.
	Parametro de entrada: int
    Valor de retorno: int
    """
    i = 0
    fat = 1
    n2 = n
    while i < n:
        fat = fat * n2
        n2 = n2 - 1
        i = i + 1
    return fat