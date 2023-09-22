#Start your python function here
def filtra_pares(a):
    t = []
    for i in a:
        if i%2==0:
            t.append(i)
    return(tuple(t))