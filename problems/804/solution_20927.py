def filtra_pares(num):
    if num[0] % 2 == 0:
        x = num[0]
    elif num[1] % 2 == 0:
        y = num[1]
    elif num[2] % 2 ==0:
        z = num[2]
    elif num[3] % 2==0:
        w = num[3]
        return (x,y,z,w,)