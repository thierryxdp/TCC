def filtra_pares(n):
    """função que retorna uma tupla com apenas elementos pares da tupla original; int, int, int, int -> tuple"""
    n=(n[0],n[1],n[2],n[3])
    pares=()
    if n[0]%2==0:
        pares = pares +(n[0],)
    if n[1]%2==0:
        pares = pares+(n[1],)
    if n[2]%2==0:
        pares = pares+(n[2],)
    if n[3]%2==0:
        pares = pares+ (n[3],)
    return pares