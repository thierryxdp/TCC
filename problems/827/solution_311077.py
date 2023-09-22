def qtd_divisores(n):
    """Mostra divisores de um número."""
    j=j
    for i in range(1,n+1):
        if (n % i) == 0:
            j=j+1
    return j