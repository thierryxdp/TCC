#Start your python function here
def filtra_pares(x, y, z, h):
    if x % 2 == 0:
        return (x,)
    if x % 2 == 0 and y % 2 == 0:
        return (x, y,)
    if x % 2 == 0 and y % 2 == 0 and z % 2 == 0:
        return (x, y, z,)
    if x % 2 == 0 and y % 2 == 0 and z % 2 == 0 and h % 2 == 0:
        return (x, y, z, h)
    if y % 2 == 0:
        return (y,)
    if y % 2 == 0 and z % 2 == 0:
        return(y, z,)
    if y % 2 == 0 and h % 2 == 0:
        return (y, h,)
    if z % 2 == 0:
        return (z,)
    if z % 2 == 0 and x % 2 == 0:
        return (x, z,)
    if z % 2 == 0 and h % 2 == 0:
        return (z, h,)
    if h % 2 == 0:
        return (h,)
    if h % 2 == 0 and x % 2 == 0:
        return (x, h,)