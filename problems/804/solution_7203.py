#Start your python function here
def filtra_pares(n1,n2,n3,n4):
    if n1 % 2 == 0:
        return n1
    if n2 % 2 == 0:
        return n2
    if n3 % 3 == 0:
        return n3
    if n4 % 4 == 0:
        return n4
    else:
        return