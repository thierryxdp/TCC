#Start your python function here
def filtra_pares(t):
    w=t[0:2]
    x=t[3:4]
    y=t[5:6]
    z=t[7:8]
    
    if (w %2)+1==0:
        return w
    elif x %2==0:
        return x