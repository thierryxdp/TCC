def faltante(listaL):
    
    listaL.sort()
    i = 0
    L1 = listaL[0]
    L2 = len(listaL) + 1
    listaCop = list(range(L1, L2)
    resposta = listaL[::-1]
    
   while i < len(listaL):
        if listaL[i] != listaCop[i]:
            return listaCop[i]
        
      	else:
            resposta = listaL[::-1]
            resposta = int(resposta) + 1
            return resposta
        i = i + 1'''

    
    return resposta