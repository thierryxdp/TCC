def filtra_pares(x):
    """Filtra apenas os numeros pares da tupla x"""           
    return ( n for n in x if n % 2 != 0 )