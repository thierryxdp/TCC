def filtra_pares(tup):
    par = tup[0]//2
    par1 = tup[1]//2
    par2 = tup[2]//2
    par3 = tup[3]//2
    nova_tup = ()
    if par1 == 0 or par2 == 0 or par3 == 0:
        nova_tup = (tup[0],tup[1],tup[2],tup[3])
        return nova_tup