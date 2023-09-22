def filtra_pares(a):
    '''Função que retorna, em uma tupla, apenas os valores pares de uma tupla inserida
        tuple -> tuple'''
    x=a[0]
    y=a[1]
    z=a[2]
    w=a[3]
    if x%2==0 and y%2==0 and z%2==0 and w%2==0:
        return (x,y,z,w)
    if x%2!=0:
        return (y,z,w)
    if y%2!=0:
        return (x,z,w)
    if z%2!=0:
        return (x,y,w)
    if w%2!=0:
        return (x,y,z)
    if x%2!=0 and y%2!=0:
        return (z,w)
    if x%2!=0 and z%2!=0:
        return (y,w)
    if x%2!=0 and w%2!=0:
        return (y,z)
    if y%2!=0 and z%2!=0:
        return (x,w)
    if y%2!=0 and w%2!=0:
        return (x,z)
    if z%2!=0 and w%2!=0:
        return (x,y)
    if x%2!=0 and y%2!=0 and z%2!=0:
        return (w)
    if x%2!=0 and y%2!=0 and w%2!=0:
        return (z)
    if x%2!=0 and z%2!=0 and w%2!=0:
        return (y)
    if y%2!=0 and z%2!=0 and w%2!=0:
        return (x)
    if x%2!=0 and y%2!=0 and z%2!=0 and w%2!=0:
        return ()