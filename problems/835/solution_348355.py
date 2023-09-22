def melhor_volta(matriz):
    listaTempo=list()
	for corredor in matriz:
        for tempo in corredor:
            listaTempo.append(tempo)
        menorTempo=min(listaTempo)
        listaAux.append(menorTempo)
    return listaAux