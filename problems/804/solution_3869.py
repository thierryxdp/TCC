#Start your python function here
def filtra_pares(x):
    """tuple->tuple"""
    a=x[0]
    b=x[1]
    c=x[2]
    d=x[3]
   v=()
    if a%2==0:
        v=v+(a,)
    elif b%2==0:
        v=v+(b,)
    elif c%2==0:
        v=v+(c,)
    elif d%2==0:
        v=v+(d,)
    return v