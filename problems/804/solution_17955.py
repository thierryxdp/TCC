#Start your python function here
def filtra_pares(a,b,c,d):
    num = (a,b,c,d)
    if num[0] % 2 == 0:
        lado = lado + (num[0],)

    if num[1] % 2 == 0:
        lado = lado + (num[1],)

    if num[2] % 2 == 0:
        lado = lado + (num[2],)

    if num[3] % 2 == 0:
        lado = lado + (num[3],)

    return lado