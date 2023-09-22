def melhor_volta(matriz):
    listaTempo=list()
    listaMenorTempo=list()
	for corredor in matriz:
        menorTempo=min(corredor)
        listaMenorTempo.append(menorTempo)
    return min(listaMenorTempo), list.index(listaMenorTempo,min(listaMenorTempo))