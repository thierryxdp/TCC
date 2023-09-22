def qtd_divisores(n):
    """Mostra divisores de um número."""
    div = []
    for i in range(n,n+1):
        if i % 2 ==0:
            div.append(i)
            return div