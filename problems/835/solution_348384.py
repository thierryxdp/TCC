def melhor_volta(m):
    lista=[]
    for elementos in m:
        menorTempo=min(elementos) 
        indice=list.index(elementos, menorTempo)
        lista.append(elementos)
        lista.append(menorTempo)
    return lista