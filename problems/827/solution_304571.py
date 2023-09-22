def qtd_divisores (n):
    """Recebe um número e retorna quantos divisores ele 
    possui.
    int -> int"""
    n_divisores = []
    for x in range(1, n+1):
        if n % x == 0:
            list.append (n_divisores, x)
    return len(n_divisores)