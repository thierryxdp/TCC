def filtra_pares(A):
    """retorna apenas os elementos pares da tupla original
    tuple -> tuple"""
    if A[0]%2 == 0:
        sub0 = A[0]
    elif A[1]%2 == 0:
        sub1 = A[1]
    elif A[2]%2 == 0:
        sub2 = A[2]
    elif A[3]%2 == 0:
        sub3 = A[3]
    else:
        return ()
    return sub0, sub1, sub2, sub3