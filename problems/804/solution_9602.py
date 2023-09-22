def filtra_pares(tupla):
	ind0 = tupla[0]%2
    ind1 = tupla[1]%2
    ind2 = tupla[2]%2
    ind3 = tupla[3]%2
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
                if ind3 == 0:
                    par = par + ((tupla[3]),)
    return par