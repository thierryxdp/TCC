def melhor_volta(matriz):
	for corredor in matriz:
        for tempo in corredor:
            listaTempo.append(tempo)
        menorTempo=min(listaTempo)
        listaAux.append(menorTempo)
    return listaAux