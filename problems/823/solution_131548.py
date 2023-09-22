def faltante(listaL):
    
    listaL.sort()
    i = 0
    L1 = listaL[0]
    L2 = len(listaL) + 1
    listaCop = list(range(L1, L2))
    
    if listaL == listaCop:
    	return listaCop[-1] + 1
                    
    while listaCop[i] in listaL:
        if listaCop[i] != 1:
            return 1
       	i = i + 1
                    
    return listaCop[i]