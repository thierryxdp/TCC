def melhor_volta(matriz):
    listaTempo=list()
    listaAux=list()
	for corredor in matriz:
        menorTempo=min(corredor)
        listaAux.append(menorTempo)
    return listaAux