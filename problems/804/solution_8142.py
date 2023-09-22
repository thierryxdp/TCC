def filtra_pares(tupla):
    (x, y, z, h) = tupla
    if x % 2 == 0 and y % 2 == 0 and z % 2 == 0 and h % 2 == 0:
        return (x, y, z, h)
    if x % 2 == 0 and y % 2 == 0 and z % 2 == 0:
        return (x, y, z)
    if x % 2 == 0 and y % 2 == 0 and h % 2 == 0:
        return (x, y, h)
    if x % 2 == 0 and z % 2 == 0 and h % 2 == 0:
        return (x, z, h)
    if y % 2 == 0 and z % 2 == 0 and h % 2 == 0:
        return (y, z, h)
    if x % 2 == 0 and y % 2 == 0:
        return (x, y)
    if x % 2 == 0 and z % 2 == 0:
        return (x, z)
    if x % 2 == 0 and h % 2 == 0:
        return (x, h)
    if y % 2 == 0 and z % 2 == 0:
        return (y, z)
    if y % 2 == 0 and h % 2 == 0:
        return (y, h)
    if z % 2 == 0 and h % 2 == 0:
        return (z, h)
    if x % 2 == 0:
        return (x,)
    if y % 2 == 0:
        return (y,)
    if z % 2 == 0:
        return (z,)
    if h % 2 == 0:
        return (h,)
    else:
        return ()