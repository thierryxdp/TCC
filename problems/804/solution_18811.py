def filtra_pares(n):
    fim = ()
    if n[0] % 2 == 0:
        fim = fim + (n[0], )
    if n[1] % 2 == 0:
        fim = fim + (n[1], )
    if n[2] % 2 == 0:
        fim = fim + (n[2], )
    if n[3] % 2 == 0:
        fim = fim + (n[3], )
    
    return fim