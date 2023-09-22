def filtra_pares(x,y,z,w):
    """Função em que dados 4 números inteiros x y z w retorna uma tupla contendo somente on números pares.
    int, int, int, int -> int,int,int,int"""
    if x%2==0:
        i1=x
        else:
            i1=0
    if y%2==0:
        i2=y
        else:
            i2=0
    if z%2==0:
        i3=z
        else:
            i3=0
    if w%2==0:
        i4=w
        else:
            i4=0

    return i1,i2,i3,i4