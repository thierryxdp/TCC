def qtd_divisores(n):
    """Retorna um inteiro que expressa a quantidade de divisores
    que um determinado número dado como entrada possui.
    int -> int"""
    qtd = 0
    for numero in range(1, n+1):
        if n%numero == 0:
            qtd +=1
    return qtd