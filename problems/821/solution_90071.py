def fatorial(n):
    """
    Essa função recebe um número n e retorna o fatorial de n;
    int -> int
    """
    resultado = 1
    for i in range(1, n+1):
        resultado = resultado * i
    return resultado