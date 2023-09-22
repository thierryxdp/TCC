#Start your python function here
def filtra_pares(t):
    y=()
    if (t[0]%2==0):
        y=(t[0],)
        if (t[1]%2==0):
            y=y+(t[1],)
            if (t[2]%2==0):
                y=y+(t[2],)
                if (t[3]%2==0):
                    y=y+(t[3],)
                    return y