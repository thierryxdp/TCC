def melhor_volta(matriz):
    listaTempo=list()
    listaAux=list()
	for corredor in matriz:
        listaTempo.append(corredor)
        menorTempo=min(listaTempo)
        listaAux.append(menorTempo)
    return listaAux