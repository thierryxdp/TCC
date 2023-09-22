def filtra_pares(a,b,c,d):
    x = ()
    if (a%2 == 0):
        x = (a,)
        elif (b%2 == 0):
            x = (a,b)
            elif (c%2 == 0):
                x = (a,b,c)
                elif (d%2 == 0):
                    x = (a,b,c,d)
                    return x