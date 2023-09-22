def faltante(listaL):
    
    listaL.sort()
    i = 0
    listaCop = range(listaL[0], len(listaL))
    
    #while i < len(listaL):
    #    if listaL[i] != listaCop[i]:
    #        return listaCop[i]
    #    i = i + 1
    listA = []
    listA[0] = listaL
    listA[1] = listaCop
    
    return listA