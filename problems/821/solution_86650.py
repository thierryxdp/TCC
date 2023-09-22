def fatorial (n):
    """Essa funcao, dado um numero, calcula e retorna o seu fatorial
    int -> int""""
	i = 1
    f = 1
    while i < n:
        i = i + 1
        f *= i
    return f