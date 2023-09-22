def filtra_pares(a,b,c,d):
    """retorne somente os números pares dos elementos de entrada"""
    pares=()
    if a%2==0 and b%2==0 and c%2==0 and d%2==0:
        novospares = pares+a,b,c,d
        return novospares