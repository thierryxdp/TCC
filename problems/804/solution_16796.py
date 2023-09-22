def filtra_pares(tup):
    x1=tup[0]%2
    x2=tup[1]%2
    x3=tup[2]%2
    x4=tup[3]%2
    if x1==0:
        z1=tup[0]
    else:
        z1=()
    if x2==0:
        z2=tup[1]
    else:
        z2=()
    if x3==0:
        z3=tup[2]
    else:
        z3=()
    if x4==0:
        z4=tup[3]
    else:
        z4=()
        return z1,z2,z3,z4
#Start your python function here