def faltante(listaL):
    
    listaL.sort()
    i = 0
    listaCop = list(range(listaL[0], len(listaL)))
    
    #while i < len(listaL):
    #    if listaL[i] != listaCop[i]:
    #        return listaCop[i]
    #    i = i + 1
    listA = []
    listA.append(listaL)
    listA.append(listaCop)
    
    return listA