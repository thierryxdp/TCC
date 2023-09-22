def filtra_pares(a):
    x,y,z,w=a
    if (x or y or z or w)%2==0:
        return (x,y,z,w)