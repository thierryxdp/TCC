def filtra_pares(s):
    y=()
    if (s[0]%2==0):
        y=(s[0],)
    elif (s[1]%2==0):
        y=y+(s[1],)
    elif (s[2]%2==0):
        y=y+(s[2],)
    elif (s[3]%2==0):
        y=y+(s[3],)
        return y