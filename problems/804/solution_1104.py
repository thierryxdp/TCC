def filtra_pares(a,b,c,d):
    """retmo os numeros pares de uma determinada tulpa"""
    pares=filter(lambda n: n % 2 == 0,a,b,c,d)
    return (pares)