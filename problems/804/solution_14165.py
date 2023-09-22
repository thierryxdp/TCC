#Start your python function here
def filtra_pares(a,b,c,d):
    tupla = ()
    if a//2==0:
        tupla+(a,)
    elif b//2==0:
        tupla+(b,)
    elif c//2==0:
        tupla+(c,)
    elif d//2==0:
        tupla+(d,)
    return tupla