def qtd_divisores(n):
    """Mostra divisores de um número."""
    div = 0
    for i in range(n,n+1):
        if i % 2 ==0:
            div += 1
            return div