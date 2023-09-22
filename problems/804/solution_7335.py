def filtra_pares([x, y, z, w]):	
    if x % 2 == 0 and y % 2 != 0 and z % 2 != 0 and w % 2 != 0:
        return ([x])
    elif x % 2 != 0 and y % 2 == 0 and z % 2 != 0 and w % 2 != 0:
        return ([y])
    elif x % 2 != 0 and y % 2 != 0 and z % 2 == 0 and w % 2 != 0:
        return ([z])
    elif x % 2 != 0 and y % 2 != 0 and z % 2 != 0 and w % 2 == 0:
        return ([w])
    elif x % 2 == 0 and y % 2 == 0 and z % 2 != 0 and w % 2 != 0:
        return ([x, y])
    elif x % 2 == 0 and y % 2 != 0 and z % 2 == 0 and w % 2 != 0:
        return ([x, z])
    elif x % 2 == 0 and y % 2 != 0 and z % 2 != 0 and w % 2 == 0:
        return ([x, w])
    elif x % 2 != 0 and y % 2 == 0 and z % 2 == 0 and w % 2 != 0:
        return ([y, z])
    elif x % 2 != 0 and y % 2 == 0 and z % 2 != 0 and w % 2 == 0:
        return ([y, w])
    elif x % 2 != 0 and y % 2 != 0 and z % 2 == 0 and w % 2 == 0:
        return ([z, w])
    elif x % 2 == 0 and y % 2 == 0 and z % 2 == 0 and w % 2 != 0:
        return ([x, y, z])
    elif x % 2 == 0 and y % 2 == 0 and z % 2 != 0 and w % 2 == 0:
        return ([x, y, w])
    elif x % 2 == 0 and y % 2 != 0 and z % 2 == 0 and w % 2 == 0:
        return ([x, z, w])
    elif x % 2 != 0 and y % 2 == 0 and z % 2 == 0 and w % 2 == 0:
        return ([y, z, w])
    elif x % 2 == 0 and y % 2 == 0 and z % 2 == 0 and w % 2 == 0:
        return ([x, y, z, w])
    else:
        return ([])