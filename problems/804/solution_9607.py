def filtra_pares(tupla):
	ind0, ind1, ind2, ind3 = tupla[0]%2, tupla[1]%2, tupla[2]%2, tupla[3]%2
    par = ()
    if ind0 == 0:
        par = ((tupla[0]),)
    else:
        par = par
    if ind1 == 0:
        par = par + ((tupla[1]),)
    else:
        par = par
    if ind2 == 0:
        par = par + ((tupla[2]),)
    else:
        par = par
    if ind3 == 0:
        par = par + ((tupla[3]),)
    else:
         par = par
    return par