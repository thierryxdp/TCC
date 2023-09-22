#Start your python function here
def filtra_pares(t)
par = (t[0] % 2 == 0)
if not t:
        return 0
if par:
        return 1 + pares(t[1:])
    else:
        return pares(t[1:])