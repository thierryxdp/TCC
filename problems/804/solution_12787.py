#Start your python function here


def filtra_pares(a):
    if a[0] %2 == 0:
       return a[0]
    elif a[1] %2 == 0:
       return a[1]
    elif a[2] %2 == 0:
       return a[2]
    else:
       return a[3]