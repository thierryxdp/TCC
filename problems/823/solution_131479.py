def faltante(listaL):
    
    listaL.sort()
    i = 0
    L1 = listaL[0]
    L2 = listaL[-1] + 1
    listaCop = list(range(L1, L2))
    
    while i < len(listaL):
        if listaL[0] != 1:
            return 1
        
        elif len(listaL) != len(listaCop):
            return listaCop[i]
        
        else:
            resposta = listaL[-1] + 1
            return resposta
        
        i = i + 1