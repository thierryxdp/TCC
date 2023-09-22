def qtd_divisor(n):
    """..."""
    i = 1
    resultado = 0
    for i in n:
        if n % i == 0 :
            resultado = resultado + i
            i = i+1
    return resultado