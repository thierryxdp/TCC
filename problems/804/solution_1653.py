def filtra_pares(x,y,z,w):
    if (x%2 and y%2 and z%2 and w%2) == 0:
        return x,y,z,w
    if (x%2 and y%2 and z%2) == 0 and w%2 !=0:
        return x,y,z