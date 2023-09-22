def qtd_divisor(n):
    """..."""
    cont = 0
    for i in range(1 , n+1):
        if n % i == 0:
            cont +=1
    return cont