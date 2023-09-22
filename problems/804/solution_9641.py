#Start your python function here
def filtra_pares(s):
    """função que filtra os números pares em uma tupla"""
    z1 = s[0]
    z2 = s[1]
    z3 = s[2] 
    z4 = s[3]
    if z1/2 == z1//2 and z2/2 == z2//2 and z3/2 == z3//2 and z4/2 == z4//2: 
        return z1, z2, z3, z4
    if z1/2 == z1//2 and z2/2 == z2//2 and z3/2 == z3//2:
        return z1, z2, z3
    if z1/2 == z1//2 and z3/2 == z3//2:
        return z1, z3
    if z1/2 == z1//2 and z2/2 == z2//2:
        return z1, z2