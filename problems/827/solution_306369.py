def qtd_divisores(n):
    """..."""
    cont=0
    for x in range(1,n+1):
        if n % x ==0:
            cont += 1
    return cont