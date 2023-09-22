def filtra_pares(a):
    """função que retorna apenas os elementos pares de uma tupla
    tuple -> tuple"""
    if int(a[0])%2==0 and int(a[1])%2==0 and int(a[2])%2==0 and int(a[3])%2==0:  
        return a
    if int(a[0])%2==0:
        return a[0]