#Start your python function here
def filtra_pares(x):
    """Dado na entrada uma tupla com quatro elementos, retorna uma tupla com apenas os elementos pares
    tuple->tuple"""
    a = x[0]
    b = x[1]
    c = x[2]
    d = x[3]
    v = ()
    if a%2==0:
        v=v+(a,)
    if b%2==0:
        v=v+(b,)
    if c%2==0:
        v=v+(c,)
    if d%2==0:
        v=v+(d,)
    return v