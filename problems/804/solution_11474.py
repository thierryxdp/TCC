def filtra_pares(a):
    '''Função que retorna, em uma tupla, apenas os valores pares de uma tupla inserida
        tuple -> tuple'''
    x=a[0]
    y=a[1]
    z=a[2]
    w=a[3]
    if x%2==0 and y%2==0 and z%2==0 and w%2==0:
        return a[0:4]
    if x%2!=0:
        return a[1:4]
    if y%2!=0:
        return (x,z,w)
    if z%2!=0:
        return (x,y,w)
    if w%2!=0:
        return a[0:3]
    if x%2!=0 and y%2!=0:
        return a[2:4]
    if x%2!=0 and z%2!=0:
        return (y,w)
    if x%2!=0 and w%2!=0:
        return a[1:3]
    if y%2!=0 and z%2!=0:
        return (x,w)
    if y%2!=0 and w%2!=0:
        return (x,z)
    if z%2!=0 and w%2!=0:
        return a[0:2]
    if x%2!=0 and y%2!=0 and z%2!=0:
        return (w)
    if x%2!=0 and y%2!=0 and w%2!=0:
        return (z)
    if x%2!=0 and z%2!=0 and w%2!=0:
        return (y)
    if y%2!=0 and z%2!=0 and w%2!=0:
        return (x)