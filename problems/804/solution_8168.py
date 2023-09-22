def filtra_pares(tupla):
    par = tupla[0]%2 == 0
    par1 = tupla[1]%2 == 0
    par2 = tupla[2]%2 == 0
    par3 = tupla[3]%2 == 0
    if par and par1 and par2 and par3:
        return tupla