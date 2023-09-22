def filtra_pares(s):
    if (s[0]%2==0):
        y=(s[0],)
        else:
            y=()
    if (s[1]%2==0):
        y=y+(s[1],)
        else:
            y=()
    if (s[2]%2==0):
        y=y+(s[2],)
        else:
            y=()
    if (s[3]%2==0):
        y=y+(s[3],)
        else:
            y=()
        return y