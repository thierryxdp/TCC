def filtra_pares(tup):
    par = tup[0]%2
    par1 = tup[1]%2
    par2 = tup[2]%2
    par3 = tup[3]%2
    if par == 0 and par3 == 0:
        return (tup[0],tup[3],)
    elif par == 0 and par2 == 0 and par3 == 0:
        return (tup[0],tup[2],tup[3],)
    elif par == 0:
        return (tup[0],)
    elif par3 == 0:
        return (tup[3],)
    elif (par and par1 and par2 and par3) != 0:
        return ()
    elif par == 0 and par1 == 0 and par2== 0 and par3 == 0:
        return (tup[0],tup[1],tup[2],tup[3],)