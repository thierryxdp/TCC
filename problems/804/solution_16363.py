#Start your python function here
def filtra_pares(s):
    """tup->tup"""
    y=()
    if (s[0]%2==0):
        return y=(s[0],)
        if (s[1]%2==0):
            return y=y+(s[1],)
            if (s[2]%2==0):
                return y=y+(s[2],)
                if (s[3]%2==0):
                    return y=y+(s[3],)