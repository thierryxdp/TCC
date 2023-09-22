#Start your python function here
def filtra_pares(tupla):
    y = ()
    for i in tupla:
        if (i==0 or (i*-1)%2==0):
            print(i)
            y = y + (i,)
    return y