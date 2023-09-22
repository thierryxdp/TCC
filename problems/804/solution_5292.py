#Start your python function here
def filtra_pares(t):
    p=(t[0:3]%2==0)
    if p:
        return 1 + filtra_pares(t[1:])
    else:
        return filtra_pares(t[1:])