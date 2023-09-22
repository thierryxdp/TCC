def faltante(listaL):
    
    listaL.sort()
    i = 0
    listaCop = list(range(listaL[0], len(listaL) + 1))
    
    while i < len(listaL):
        if listaL[i] != listaCop[i]:
            return listaCop[i]
        
        elif listaL in listaCop:
            resposta = listaL[::-1] + 1
            return resposta
        i = i + 1

    
    return