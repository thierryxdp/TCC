def melhor_volta(matriz):
	i=0
    listaAux=[]
    lista=[]
    for corredores in matriz:
        menorTempo=min(corredores)
        i=list.index(corredores,menorTempo)
    	listaAux.append(i)
        listaAux.append(menorTempo)
    lista.append(listaAux)
    return lista