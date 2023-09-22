#Start your python function here
def filtra_pares(a,b,c,d):
    num = (a,b,c,d)
    if num[0] % 2 == 0:
        lado = lado + (num[0],)

    elif num[1] % 2 == 0:
        lado = lado + (num[1],)

    elif num[2] % 2 == 0:
        lado = lado + (num[2],)

    elif num[3] % 2 == 0:
        lado = lado + (num[3],)

    return lado