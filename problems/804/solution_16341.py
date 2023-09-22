#Start your python function here
def filtra_pares(s):
    y=()
    if (s[0]%2==0):
        y=(s[0],)
        if (s[1]%2==0):
            y=y+(s[1],)
            if (s[2]%2==0):
                y=y+(s[2],)
                if (s[3]%2==0):
                    y=y+(s[3],)
                    return y[]