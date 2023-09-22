def par (n):
    if n%2==0:
        return n
def filtra_pares(n):
    if n%2==0:
        return list(filter(filtra_pares,n))