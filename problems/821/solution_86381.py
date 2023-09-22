def fatorial(n):
    """dado um número, função retorna o fatorial desse número. int -> int"""
    resultado = 1
    f = 1

    while f <= n:
        resultado = resultado * f
        f = f + 1
    return resultado