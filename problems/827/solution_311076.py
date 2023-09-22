def qtd_divisores(n):
    """Mostra divisores de um número."""
    for i in range(1,n+1):
        if (n % i) == 0:
            print (i)