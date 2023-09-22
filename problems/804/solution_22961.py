def filtra_pares(a):
    pares=tuple(it for it in a if it[0]%2==0)
    return pares