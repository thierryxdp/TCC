def filtra_pares(a,b,c,d):
    """retorna apenas os elementos pares dos paremetros
    a, b, c e d de entrada.
    int, int, int, int -> tupla"""
    if a%2==0:
        return (a)
    if a%2==0 and b%2==0:
        return (a,b)
    if a%2==0 and b%2==0 and c%2==0:
        return (a,b,c)
    if a%2==0 and b%2==0 and c%2==0 and d%2==0:
        return (a,b,c,d)