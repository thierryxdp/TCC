def qtd_divisor(n):
    """..."""
    divisor = 0 
    for i in range(1,n,-1):
        divisor = divisor + i
    i += 1
    return divisor