ef filtra_pares(a,b,c,d):
    """recebe uma tupla T composta de 4 numeros inteiros, retornando apenas seus
elementos pares; int -> int."""
    R = ()
    if a % 2 == 0: R = (a,)
    if b % 2 == 0: R = R[:] + (b,)
    if c % 2 == 0: R = R[:] + (c,)
    if d % 2 == 0: R = R[:] + (d,)
    return R#Start your python function here