#Start your python function here
def filtra_pares(s):
    """função que filtra os números pares em uma tupla"""
    z1 = s[0]
    z2 = s[1]
    z3 = s[2] 
    z4 = s[3]
    if z1/2 == z1//2 or z2/2 == z2//2 or z3/2 == z3//2 or z4/2 == z4//2:
        return str(z1) + str(z2) + str(z3) + str(z4)