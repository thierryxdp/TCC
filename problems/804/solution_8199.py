def filtra_pares(tupla):
    a= tupla[0]
    b= tupla[1]
    c= tupla[2]
    d= tupla[3]
    par = tupla[0]%2 == 0
    par1 = tupla[1]%2 == 0
    par2 = tupla[2]%2 == 0
    par3 = tupla[3]%2 == 0
    if par and par1 and par2 and par3:
        return a,b,c,d
    if par and par1 and par2 and not par3:
        return a,b,c
    if par and par1 and not par2 and not par3:
        return a,b,
    if par and not par1 and not par2 and not par3:
        return a,
    if not par and par1 and par2 and par3:
        return b,c,d
    if not par and par1 and par2 and not par3:
        return b,c
    if not par and par1 and not par2 and not par3:
        return b
    if not par and not par1 and  par2 and  par3:
        return c,d
    if not par and not par1 and  par2 and not  par3:
        return c,
    if not par and not par1 and not par2 and par3:
        return d,
    if par and not par1 and  par2 and  par3:
        return a,c,d
    if par and not par1 and  par2 and not par3:
        return a,c
    if par and not par1 and not par2 and par3:
        return a,d
    if not par and not par1 and not par2 and not par3:
            return ()