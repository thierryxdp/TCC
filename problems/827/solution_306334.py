def qtd_divisor(n):
    """..."""
    i = 1
    soma = 0
    for i in n:
        if n % i:
            soma = soma + i
    i = i+1
    return soma