def filtra_pares(T):
    """recebe uma tupla T composta de 4 numeros inteiros, retornando apenas seus
elementos pares; int -> int."""
    a,b,c,d = T
    R = ()
    if T[0] % 2 == 0: R = (a,)
    if T[1] % 2 == 0: R = R[:] + (b,)
    if T[2] % 2 == 0: R = R[:] + (c,)
    if T[3] % 2 == 0: R = R[:] + (d,)
    return R