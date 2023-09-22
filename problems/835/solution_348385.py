def melhor_volta(m):
    lista=[]
    for elementos in m:
        menorTempo=min(elementos) 
        indice=list.index(elementos, menorTempo)
        lista.append(indice)
        lista.append(menorTempo)
    return lista