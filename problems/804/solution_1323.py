def filtra_pares(e1,e2,e3,e4):
    if (e1 % 2 == 0):
        if (e2 % 2 == 0):
            if (e3 % 2 == 0):
                if (e4 % 2 == 0):
                    return(e1,e2,e3,e4)
                else:
                    return(e1,e2,e3)
            elif (e4 % 2 == 0):
                return(e1,e2,e4)
            else:
                return(e1,e2)